from dataclasses import dataclass

from src.domain.profile.i_profile_presenter import IProfilePresenter
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.base.i_use_case import IUseCase

from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository

class GetUserByEmail(IUseCase):
    account_repository: IAccountRepository
    presenter: IProfilePresenter
    account_presenter: IAccountPresenter
    
    def __init__(
        self,
        account_repository: IAccountRepository,
        presenter: IProfilePresenter,
        account_presenter: IAccountPresenter
    ) -> None:
        self.account_repository = account_repository
        self.presenter = presenter
        self.account_presenter = account_presenter
    
    @dataclass
    class Response:
        user: User
    
    async def execute(self, email: str) -> Response:
        user: User = self.account_repository.get_by_email(email=email)
        if not user:
            return self.account_presenter.output_error_user_not_found()
        return self.presenter.output_view_current_user(user)
        
            