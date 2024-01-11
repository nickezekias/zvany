from sqlalchemy import Boolean, Column, DateTime, String

from src.app.db.base_class import Base


class UserORM(Base):
    """ORM object for users table"""
    __tablename__ = "users" # type: ignore

    id = Column(String(36), primary_key=True, index=True)
    avatar = Column(String, nullable=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    email_verified_at = Column(DateTime, nullable=True)
    phone_verified_at = Column(DateTime, nullable=True)
    ID_document = Column(String, nullable=True)
    ID_document_verified_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean(), default=1, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def asdict(self):
        """Model dump"""
        return {
            "id": self.id,
            "avatar": self.avatar,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
