from dataclasses import dataclass
from sqlalchemy import String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass
class ExerciseRecord:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    workout_session_id: Mapped[int] = mapped_column(Integer, ForeignKey("workout_session.id"), nullable=False)
    exercise_name: Mapped[str] = mapped_column(String(100), nullable=False)
    muscle_group: Mapped[str] = mapped_column(String(100), nullable=False)
    sets: Mapped[int] = mapped_column(Integer, nullable=False)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    weight_kg: Mapped[float] = mapped_column(Float, nullable=True)
    distance_km: Mapped[float] = mapped_column(Float, nullable=True)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    def __post_init__(self):
        if self.exercise_name is None or self.exercise_name.strip() == "":
            raise ValueError("Exercise name cannot be empty.")
        if self.sets <= 0:
            raise ValueError("Sets must be a positive value.")
        if self.reps <= 0:
            raise ValueError("Reps must be a positive value.")
        if self.weight_kg is not None and self.weight_kg < 0:
            raise ValueError("Weight must be a non-negative value.")
        if self.distance_km is not None and self.distance_km < 0:
            raise ValueError("Distance must be a non-negative value.")
        if self.duration_minutes is not None and self.duration_minutes < 0:
            raise ValueError("Duration must be a non-negative value.")

    workout_session = relationship("WorkoutSession", backref="exercise_records")