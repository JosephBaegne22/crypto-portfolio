from pydantic import BaseModel, EmailStr

# -------- USER --------
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


# -------- AUTH --------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# -------- PORTFOLIO --------
class CryptoAssetCreate(BaseModel):
    name: str
    symbol: str
    quantity: float

class CryptoAssetResponse(BaseModel):
    id: int
    name: str
    symbol: str
    quantity: float
    price: float
    value: float

    class Config:
        from_attributes = True
