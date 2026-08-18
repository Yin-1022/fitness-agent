from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

@dataclass
class BodyMeasurement:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(100), ForeignKey("user_profile.id"), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    weight_kg: Mapped[float] = mapped_column(Float, nullable=False)
    body_fat_percentage: Mapped[float] = mapped_column(Float, nullable=True)
    body_fat_mass_kg: Mapped[float] = mapped_column(Float, nullable=True)
    bmi: Mapped[float] = mapped_column(Float, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user_profile = relationship("UserProfile", backref="body_measurements")