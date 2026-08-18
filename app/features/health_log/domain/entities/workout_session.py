from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class WorkoutSession:
    id: str
    user_id: str
    date: datetime
    duration_minutes: int
    workout_type: str
    muscle_groups: list[str]
    intensity_level: str
    source: str
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self):
        if self.user_id is None or self.user_id.strip() == "":
            raise ValueError("User ID cannot be empty.")
        if self.duration_minutes <= 0:
            raise ValueError("Duration must be a positive value.")
        if self.intensity_level<1 or self.intensity_level>10:
            raise ValueError("Intensity level must be between 1 and 10.")
        if self.workout_type is None or self.workout_type.strip() == "":
            raise ValueError("Workout type cannot be empty.")