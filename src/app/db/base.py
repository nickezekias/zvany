# Import all the models, so that Base has them before being
# imported by Alembic
from src.app.db.base_class import Base  # noqa
from src.app.db.models.user_orm import UserORM  # noqa
