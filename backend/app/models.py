from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    assets = relationship("CryptoAsset", back_populates="owner", cascade="all, delete")


class CryptoAsset(Base):
    __tablename__ = "crypto_assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="assets")
