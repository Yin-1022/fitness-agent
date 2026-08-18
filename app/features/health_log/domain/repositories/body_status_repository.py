from abc import ABC, abstractmethod
from datetime import date
from app.features.health_log.domain.entities.body_status_log import BodyStatusLog

class BodyStatusRepository(ABC):
    @abstractmethod
    def create_body_status_log(self, log: BodyStatusLog) -> BodyStatusLog:
        ...

    @abstractmethod
    def get_body_status_logs_by_user(self, user_id: int) -> list[BodyStatusLog]:
        ...

    @abstractmethod
    def get_body_status_logs_by_date_range(self, user_id: int, start_date: date, end_date: date) -> list[BodyStatusLog]:
        ...

    @abstractmethod
    def get_body_status_log_by_date(self, user_id: int, target_date: date) -> BodyStatusLog | None:
        ...