from fastapi import APIRouter, Depends

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.profile.i_profile_presenter import IProfilePresenter
from src.domain.account.user import User

from src.app.api.api_v1.profile.adapter.presenter.profile_presenter import ProfilePresenter
from src.app.api.api_v1.account.adapter.presenter.account_presenter import AccountPresenter

from src.app.api.api_v1.profile.use_case.get_user_by_email import GetUserByEmail as GetUserByEmailUseCase

from src.app.api.api_v1.deps import get_account_mariadb_repository
from src.app.api.api_v1.deps import get_current_active_user


router = APIRouter(
    tags=["profile"]
)

@router.get("/profile/me", response_model=dict, status_code=200)
async def my_profile(
    current_user: User=Depends(get_current_active_user),
) -> dict:
    return current_user