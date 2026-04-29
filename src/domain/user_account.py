from dataclasses import dataclass


@dataclass(slots=True)
class UserAccount:
    user_id: str
    platform: str
    platform_user_id: str
