from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class BodyStatusLog:
    id: str
    user_id: str
    date: datetime
    sleep_hours: float
    sleep_quality: int
    fatigue_level: int
    stress_level: int
    created_at: datetime
    updated_at: datetime
    soreness_level: Optional[int] = None
    soreness_parts: Optional[list[str]] = None
    mood_level: Optional[int] = None
    notes: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self):
        if self.sleep_hours < 0:
            raise ValueError("Sleep hours must be a non-negative value.")
        if self.sleep_quality < 1 or self.sleep_quality > 10:
            raise ValueError("Sleep quality must be between 1 and 10.")
        if self.fatigue_level < 1 or self.fatigue_level > 10:
            raise ValueError("Fatigue level must be between 1 and 10.")
        if self.stress_level < 1 or self.stress_level > 10:
            raise ValueError("Stress level must be between 1 and 10.")
        if self.soreness_level is not None and (self.soreness_level < 1 or self.soreness_level > 10):
            raise ValueError("Soreness level must be between 1 and 10.")
        if self.mood_level is not None and (self.mood_level < 1 or self.mood_level > 10):
            raise ValueError("Mood level must be between 1 and 10.")