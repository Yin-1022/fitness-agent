from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class BodyMeasurement:
    id: str
    user_id: str
    date: datetime
    created_at: datetime
    weight_kg: Optional[float] = None
    body_fat_percentage: Optional[float] = None
    body_fat_mass_kg: Optional[float] = None
    muscle_mass_kg: Optional[float] = None
    bmi: Optional[float] = None
    notes: Optional[str] = None

    def __post_init__(self):
        if self.weight_kg is not None and self.weight_kg <= 0:
            raise ValueError("Weight must be a positive value.")
        if self.body_fat_percentage is not None and (self.body_fat_percentage < 0 or self.body_fat_percentage > 100):
            raise ValueError("Body fat percentage must be between 0 and 100.")
        if self.body_fat_mass_kg is not None and self.body_fat_mass_kg < 0:
            raise ValueError("Body fat mass must be a non-negative value.")
        if self.muscle_mass_kg is not None and self.muscle_mass_kg < 0:
            raise ValueError("Muscle mass must be a non-negative value.")
        if self.bmi is not None and self.bmi <= 0:
            raise ValueError("BMI must be a positive value.")