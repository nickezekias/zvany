from datetime import datetime, timedelta

from src.domain.account.i_register_presenter import IRegisterPresenter
from src.domain.account.i_account_presenter import IAccountPresenter
from src.domain.base.i_use_case import IUseCase
from src.domain.account.i_authenticator import IAuthenticator
from src.domain.notification.notification import Notification
from src.domain.util.i_crypto import ICrypto

from src.domain.account.user import User
from src.domain.account.i_account_repository import IAccountRepository
from src.app.api.api_v1.account.adapter.presenter.account_json_mapper import AccountJsonMapper
from src.app.api.api_v1.account.adapter.request.register_request import RegisterRequest

from src.app.api.api_v1.account.adapter.response.register_response import RegisterResponse
from src.app.api.api_v1.account.use_case.send_email_verification_link import SendEmailVerificationLink

class Register(IUseCase):
    account_repository: IAccountRepository
    register_presenter: IRegisterPresenter
    authenticator: IAuthenticator
    account_json_mapper: AccountJsonMapper
    notification: Notification
    crypto: ICrypto
    sendEmailVerificationLink: SendEmailVerificationLink

    def __init__(
            self,
            account_repository: IAccountRepository,
            register_presenter: IRegisterPresenter,
            account_presenter: IAccountPresenter,
            authenticator: IAuthenticator,
            notification: Notification,
            crypto: ICrypto
        ) -> None:
        self.account_repository = account_repository
        self.register_presenter = register_presenter
        self.authenticator = authenticator
        self.account_json_mapper = AccountJsonMapper()
        self.notification = notification
        self.crypto = crypto
        self.sendEmailVerificationLink = SendEmailVerificationLink(self.crypto, self.account_repository, account_presenter, self.notification)

    async def execute(self, form_data: RegisterRequest) -> RegisterResponse | None:
        # create user entity from form data
        user_req = form_data.user
        user_req.password = self.authenticator.get_password_hash(user_req.password) # hash user request password
        user_input = self.account_json_mapper.mapToDomain(user_req)
        user_input.is_active = False


        # check no user with same email exists
        found_user: User = self.account_repository.get_by_email(email = user_input.email)
        if found_user:
            return self.register_presenter.output_errors_email_exists()
        
        # check no user with same phone exists
        found_user: User = self.account_repository.get_by_phone(phone = user_input.phone)
        if found_user:
            return self.register_presenter.output_errors_phone_exists()
        
        #set user as active
        user_input.is_active = True

        #create token
        user_input.token = self.authenticator.create_access_token({"sub": str(user_input.email + user_input.id), "nbf": datetime.now()})

        # add user to DB
        self.account_repository.add(entity=user_input)


        # []FIXME: use unit-of-work to commit application transactions
        # commit transaction to db
        try:
            self.account_repository.commit()
            #hydrate object with saved user
        except:
            return self.register_presenter.output_errors_invalid_data()
        
        user: User = self.account_repository.get_by_email(user_input.email)

        #init and send new account notification
        try:
            await self.sendEmailVerificationLink.execute(user.email)
        except Exception as e:
            from loguru import logger
            logger.error(" ERROR SENDING EMAIL VERIFICATION LINK ")
            logger.error(str(e))
        

        return self.register_presenter.output(user)

