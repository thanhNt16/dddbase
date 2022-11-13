from fastapi import APIRouter, Depends, HTTPException, status


from app.domain.user import (
    UserNotFoundError,
    UserRepository,
    UsersNotFoundError,
    User,
)
from app.presentation.schema.user.user_error_message import (
    ErrorMessageUserNotFound,
    ErrorMessageUsersNotFound,
)

from app.infrastructure.elasticsearch.user import (
    UserQueryServiceImpl,
    UserRepositoryImpl,
)
from app.usecase.user import (
    UserQueryService,
    UserQueryUseCaseImpl,
    UserQueryUseCase,
    UserReadModel,
)

router = APIRouter()


def user_query_usecase(
    # session: Session = Depends(get_session)
) -> UserQueryUseCase:
    session = None
    user_query_service: UserQueryService = UserQueryServiceImpl(session)
    return UserQueryUseCaseImpl(user_query_service)


@router.get(
    "/user",
    # response_model=List[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUserNotFound,
        },
    },
)
async def get_user(
    user_query_usecase: UserQueryUseCase = Depends(user_query_usecase),
):
    try:
        user = user_query_usecase.fetch_user_by_id(4)

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=UserNotFoundError.message,
        )

    return user
