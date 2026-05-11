import os
import asyncio
from uuid import uuid4

from sqlalchemy import text

from session import new_session_maker

TELEGRAM_BOT_INIT_MAIN_ADMIN_ID = os.getenv("TELEGRAM_BOT_INIT_MAIN_ADMIN_ID")


async def main():
    session = new_session_maker()()
    result = await session.execute(
        text("SELECT uuid FROM users WHERE role='main_admin'")
    )
    main_admin_uuid = result.scalar_one_or_none()
    if not main_admin_uuid:
        main_admin_uuid = uuid4()
        await session.execute(
            text("INSERT INTO users(uuid, role) VALUES(:uuid, 'main_admin')"),
            {"uuid": main_admin_uuid},
        )
        await session.commit()
    result = await session.execute(
        text("SELECT * FROM user_accounts WHERE user_id=:uuid AND platform='telegram'"),
        {"uuid": main_admin_uuid},
    )
    user_telegram_account = result.fetchone()
    if not user_telegram_account:
        if not TELEGRAM_BOT_INIT_MAIN_ADMIN_ID:
            await session.close()
            raise ValueError(
                "Please set the value of TELEGRAM_BOT_INIT_MAIN_ADMIN_ID in the environment variables"
            )
        await session.execute(
            text(
                "INSERT INTO user_accounts(user_id, platform, platform_user_id) VALUES(:uuid, 'telegram', :platform_user_id)"
            ),
            {
                "uuid": main_admin_uuid,
                "platform_user_id": TELEGRAM_BOT_INIT_MAIN_ADMIN_ID,
            },
        )
        await session.commit()
    await session.close()


asyncio.run(main())
