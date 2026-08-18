from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass
class UserProfile:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    height_cm: Mapped[float] = mapped_column(Float, nullable=False)
    goal: Mapped[str] = mapped_column(String(100), nullable=False)
    weekly_training_days_goal: Mapped[int] = mapped_column(Integer, nullable=False)
    experience_level: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __post_init__(self):
        if self.name is None or self.name.strip() == "":
            raise ValueError("Name cannot be empty.")
        if self.height_cm <= 0:
            raise ValueError("Height must be a positive value.")
        if self.weekly_training_days_goal < 0 or self.weekly_training_days_goal > 7:
            raise ValueError("Weekly training days goal must be between 0 and 7.")

    workout_sessions = relationship("WorkoutSession", backref="user_profile", cascade="all, delete-orphan")
    body_status_logs = relationship("BodyStatusLog", backref="user_profile", cascade="all, delete-orphan")
    body_measurements = relationship("BodyMeasurement", backref="user_profile", cascade="all, delete-orphan")