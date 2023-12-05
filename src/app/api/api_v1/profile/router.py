from fastapi import APIRouter, Depends

from src.domain.account.i_account_repository import IAccountRepository
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.profile.i_profile_presenter import IProfilePresenter

from src.app.api.api_v1.profile.adapter.presenter.profile_presenter import ProfilePresenter
from src.app.api.api_v1.account.adapter.presenter.account_presenter import AccountPresenter

from src.app.api.api_v1.profile.use_case.get_user_by_email import GetUserByEmail as GetUserByEmailUseCase

from src.app.api.api_v1.deps import get_account_mariadb_repository



router = APIRouter(
    tags=["profile"]
)

@router.get("/profile/me", response_model=dict, status_code=200)
async def my_profile(
    email: str,
    account_repository: IAccountRepository=Depends(get_account_mariadb_repository)
) -> dict:
    account_presenter: IAccountPresenter = AccountPresenter()
    presenter: IProfilePresenter = ProfilePresenter()
    return await GetUserByEmailUseCase(account_repository=account_repository, presenter=presenter, account_presenter=account_presenter).execute(email)