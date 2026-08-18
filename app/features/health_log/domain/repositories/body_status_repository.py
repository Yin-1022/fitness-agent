from abc import ABC, abstractmethod
from datetime import date
from app.features.health_log.domain.entities.body_status_log import BodyStatusLog

class BodyStatusRepository(ABC):
    @abstractmethod
    def create_body_status_log(log: BodyStatusLog) -> BodyStatusLog:
        ...

    @abstractmethod
    def get_body_status_logs_by_user(user_id: str) -> list[BodyStatusLog]:
        ...

    @abstractmethod
    def get_body_status_logs_by_date_range(user_id: str, start_date: date, end_date: date) -> list[BodyStatusLog]:
        ...

    @abstractmethod
    def get_body_status_log_by_date(user_id: str, target_date: date) -> BodyStatusLog | None:
        ...