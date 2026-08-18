from abc import ABC, abstractmethod
from datetime import date
from app.features.health_log.domain.entities.body_measurement import BodyMeasurement

class BodyMeasurementRepository(ABC):
    @abstractmethod
    def create_body_measurement(self, measurement: BodyMeasurement) -> BodyMeasurement:
        ...

    @abstractmethod
    def get_body_measurements_by_user(self, user_id: int) -> list[BodyMeasurement]:
        ...

    @abstractmethod
    def get_body_measurements_by_date_range(self, user_id: int, start_date: date, end_date: date) -> list[BodyMeasurement]:
        ...

    @abstractmethod
    def get_latest_body_measurement(self, user_id: int) -> BodyMeasurement | None:
        ...