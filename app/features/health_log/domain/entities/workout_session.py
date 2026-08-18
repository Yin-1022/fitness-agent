from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass
class WorkoutSession:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), ForeignKey("user_profile.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    workout_type: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=True)
    muscle_groups: Mapped[list[str]] = mapped_column(Text, nullable=False)
    intensity_level: Mapped[int] = mapped_column(Integer, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __post_init__(self):
        if self.user_id is None or self.user_id.strip() == "":
            raise ValueError("User ID cannot be empty.")
        if self.duration_minutes <= 0:
            raise ValueError("Duration must be a positive value.")
        if self.intensity_level<1 or self.intensity_level>10:
            raise ValueError("Intensity level must be between 1 and 10.")
        if self.workout_type is None or self.workout_type.strip() == "":
            raise ValueError("Workout type cannot be empty.")

    user_profile = relationship("UserProfile", backref="workout_sessions")