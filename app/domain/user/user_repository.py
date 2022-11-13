from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.user.user import User


class UserRepository(ABC):
    """UserRepository defines a repository interface for User entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        raise NotImplementedError
