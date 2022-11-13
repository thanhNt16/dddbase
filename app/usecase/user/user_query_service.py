from abc import ABC, abstractmethod
from typing import List, Optional

from .user_query_model import UserReadModel


class UserQueryService(ABC):
    """UserQueryService defines a query service inteface related Book entity."""

    @abstractmethod
    def find_by_id(self, id_itilisateur: int) -> Optional[UserReadModel]:
        raise NotImplementedError
