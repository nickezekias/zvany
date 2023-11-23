from sqlalchemy import Boolean, Column, DateTime, String
from src.app.db.base_class import Base

class PRTokenORM(Base):
    __tablename__="password_reset_tokens"
    
    id = Column(String(36), primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    token = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime)
    used_at = Column(DateTime, nullable=True)
    ip_address = Column(String(15), unique=True, index=True, nullable=False)
    user_agent = Column(String, unique=True, index=True, nullable=False)
    
    def asdict(self):
        return {
            "id": self.id,
            "email": self.email,
            "token": self.token,
            "created_at": self.created_at,
            "used_at": self.used_at,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent
        }