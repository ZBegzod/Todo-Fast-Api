from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from config.database import Base
from datetime import datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime
from sqlalchemy_utils.types import ChoiceType, EmailType
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=120))
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship("User", back_populates="roles")

    def __repr__(self):
        return f"{self.name}"


class User(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(String(length=150))
    username = Column(String(length=120), unique=True, nullable=False)
    hashed_password = Column(String(), nullable=False)
    country = Column(String(length=150))
    phone_number = Column(String(length=150), unique=True, nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False, onupdate=datetime.utcnow())
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    roles = relationship("Role", back_populates="user")

    def __repr__(self):
        return f"{self.username}"
