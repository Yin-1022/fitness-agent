from datetime import datetime, date as date_type
from app.database.base import Base
from sqlalchemy import String, Integer, Float, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

class BodyStatusLogModel(Base):
    __tablename__ = "body_status_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    date: Mapped[date_type] = mapped_column(Date, nullable=False)
    sleep_hours: Mapped[float] = mapped_column(Float, nullable=False)
    sleep_quality: Mapped[int] = mapped_column(Integer, nullable=False)
    fatigue_level: Mapped[int] = mapped_column(Integer, nullable=False)
    stress_level: Mapped[int] = mapped_column(Integer, nullable=False)
    soreness_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    soreness_parts: Mapped[str | None] = mapped_column(Text, nullable=True)
    mood_level: Mapped[int | None] = mapped_column(Integer, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    source: Mapped[str] = mapped_column(String(100), nullable=False, default="manual")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    user = relationship(
        "UserModel",
        back_populates="body_status_logs",
    )