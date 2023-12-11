from src.domain.profile.i_profile_presenter import IProfilePresenter
from src.domain.account.user import User
from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper


class ProfilePresenter(IProfilePresenter):
    def output_view_current_user(self, user: User) -> dict:
        user_res = AccountJsonMapper().mapFromDomain(user)
        return {
            "user": user_res
        }