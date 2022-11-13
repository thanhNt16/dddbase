from typing import List, Optional

from app.usecase.user import UserQueryService, UserReadModel
from app.domain.user import User

from .user_dto import UserDTO


class UserQueryServiceImpl(UserQueryService):
    """UserQueryServiceImpl implements READ operations related User entity using SQLAlchemy."""

    def __init__(self, session):
        self.session = session

    def find_by_id(self, id: int) -> Optional[UserReadModel]:
        try:
            user_dto = UserDTO(id, 10)
            print("user_dto: ", user_dto)

        except Exception as e:
            print("Exception: ", e)
            return None
        except:
            raise
        print("to read", user_dto.to_entity())
        return user_dto.to_entity()
