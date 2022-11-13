from typing import Optional

from app.domain.user import User, UserRepository

from .user_dto import UserDTO


class UserRepositoryImpl(UserRepository):
    """BookRepositoryImpl implements CRUD operations related Book entity using SQLAlchemy."""

    def __init__(self, session):
        self.session = session

    def find_by_id(self, id: int) -> Optional[User]:
        try:
            user_dto = UserDTO.from_entity(User(id, 10))
        except Exception:
            return None
        except:
            raise

        return user_dto.to_entity()
