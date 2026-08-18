from abc import ABC, abstractmethod
from datetime import date
from app.features.health_log.domain.entities.workout_session import WorkoutSession
from app.features.health_log.domain.entities.exercise_record import ExerciseRecord

class WorkoutRepository(ABC):
    @abstractmethod
    def create_workout_session(self, workout_session: WorkoutSession) -> WorkoutSession:
        ...

    @abstractmethod
    def get_workout_session_by_id(self, session_id: int) -> WorkoutSession | None:
        ...

    @abstractmethod
    def get_workout_sessions_by_user(self, user_id: str) -> list[WorkoutSession]:
        ...

    @abstractmethod
    def get_workout_sessions_by_date_range(self, user_id: str, start_date: date, end_date: date) -> list[WorkoutSession]:
        ...

    @abstractmethod
    def create_exercise_record(self, record: ExerciseRecord) -> ExerciseRecord:
        ...

    @abstractmethod
    def get_exercise_records_by_session(self, session_id: int) -> list[ExerciseRecord]:
        ...