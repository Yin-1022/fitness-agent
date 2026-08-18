from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class BodyMeasurement:
    id: str
    user_id: str
    date: datetime
    weight_kg: Optional[float] = None
    body_fat_percentage: Optional[float] = None
    body_fat_mass_kg: Optional[float] = None
    muscle_mass_kg: Optional[float] = None
    bmi: Optional[float] = None
    notes: Optional[str] = None
    created_at: datetime