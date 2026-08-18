from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass
class BodyStatusLog:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), ForeignKey("user_profile.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    sleep_hours: Mapped[float] = mapped_column(Float, nullable=False)
    sleep_quality: Mapped[int] = mapped_column(Integer, nullable=False)
    fatigue_level: Mapped[int] = mapped_column(Integer, nullable=False)
    stress_level: Mapped[int] = mapped_column(Integer, nullable=False)
    soreness_level: Mapped[int] = mapped_column(Integer, nullable=True)
    soreness_parts: Mapped[list[str]] = mapped_column(Text, nullable=True)
    mood_level: Mapped[int] = mapped_column(Integer, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

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

    user_profile = relationship("UserProfile", backref="body_status_logs")