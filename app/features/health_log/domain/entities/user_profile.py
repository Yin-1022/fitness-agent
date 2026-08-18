from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserProfile:
    id: str
    name: str
    height_cm: Optional[float] = None
    goal: str
    weekly_training_days_goal: int
    experience_level: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if self.name is None or self.name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if self.height_cm <= 0:
            raise ValueError("Height must be a positive value.")
        if self.weekly_training_days_goal < 0 or self.weekly_training_days_goal > 7:
            raise ValueError("Weekly training days goal must be between 0 and 7.")