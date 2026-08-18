from abc import ABC, abstractmethod
from app.features.health_log.domain.entities.user_profile import UserProfile

class UserRepository(ABC):
    @abstractmethod
    def create_user(user: UserProfile) -> UserProfile:
        ...

    @abstractmethod
    def get_user_by_id(user_id: str) -> UserProfile | None:
        ...

    def update_user(user: UserProfile) -> UserProfile:
        ...
    