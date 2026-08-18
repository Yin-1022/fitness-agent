from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ExerciseRecord:
    id: int | None
    workout_session_id: int
    exercise_name: str
    muscle_group: str
    sets: int | None = None
    reps: int | None = None
    weight_kg: Optional[float] = None
    distance_km: Optional[float] = None
    duration_minutes: Optional[int] = None
    notes: Optional[str] = None

    def __post_init__(self):
        if self.exercise_name is None or self.exercise_name.strip() == "":
            raise ValueError("Exercise name cannot be empty.")
        if self.sets is not None and self.sets <= 0:
            raise ValueError("Sets must be a positive value.")
        if self.reps is not None and self.reps <= 0:
            raise ValueError("Reps must be a positive value.")
        if self.weight_kg is not None and self.weight_kg < 0:
            raise ValueError("Weight must be a non-negative value.")
        if self.distance_km is not None and self.distance_km < 0:
            raise ValueError("Distance must be a non-negative value.")
        if self.duration_minutes is not None and self.duration_minutes < 0:
            raise ValueError("Duration must be a non-negative value.")