from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from jinja2 import Environment, select_autoescape, PackageLoader

from src.app.config import settings

env = Environment(
    loader=PackageLoader('src.app.email', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

class EmailService:
    recipients: list[EmailStr]
    def __init__(self, recipients: list[EmailStr]):
        self.recipients = recipients

    async def sendMail(self, subject: str, template, template_data: dict):
        conf = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM_ADDRESS,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_HOST,
            MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=False,
            VALIDATE_CERTS=False
        )
        # Generate the HTML template base on the template name
        template = env.get_template(f'{template}.html')

        html = template.render(
            subject=subject,
            **template_data
        )

        # Define the message options
        message = MessageSchema(
            subject=subject,
            recipients=self.recipients,
            body=html,
            subtype="html"
        )

        # Send the email
        try:
            fm = FastMail(conf)
            await fm.send_message(message)
        except Exception as e:
            from loguru import logger
            logger.error("EMAIL SERVER ERROR")
            logger.error(e)
