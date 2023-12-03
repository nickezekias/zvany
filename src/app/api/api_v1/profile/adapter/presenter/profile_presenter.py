from src.domain.profile.i_profile_presenter import IProfilePresenter
from src.domain.account.user import User

class ProfilePresenter(IProfilePresenter):
    def output_view_current_user(self, user: User) -> dict:
        return {
            "user": user
        }