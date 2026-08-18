from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserProfile:
    id: int | None
    name: str
    goal: str
    weekly_training_days_goal: int
    created_at: datetime
    updated_at: datetime
    height_cm: Optional[float] = None
    experience_level: Optional[str] = None

    def __post_init__(self):
        if self.name is None or self.name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if self.height_cm is not None and self.height_cm <= 0:
            raise ValueError("Height must be a positive value.")
        if self.weekly_training_days_goal < 0 or self.weekly_training_days_goal > 7:
            raise ValueError("Weekly training days goal must be between 0 and 7.")