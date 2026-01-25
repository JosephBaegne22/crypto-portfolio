from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import CryptoAsset
from ..schemas import CryptoAssetCreate
from ..auth import get_current_user_id

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"]
)

# PRIX FIXES (MOCK)
CRYPTO_PRICES = {
    "BTC": 30000,
    "ETH": 2000,
    "SOL": 100,
}

# ADD ASSET
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_asset(
    asset: CryptoAssetCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    price = CRYPTO_PRICES.get(asset.symbol.upper())
    if price is None:
        raise HTTPException(status_code=400, detail="Unsupported crypto")

    new_asset = CryptoAsset(
        name=asset.name,
        symbol=asset.symbol.upper(),
        quantity=asset.quantity,
        price=price,
        user_id=user_id
    )

    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    return {"message": "Asset added successfully"}


# LIST PORTFOLIO
@router.get("/")
def get_portfolio(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    assets = db.query(CryptoAsset).filter(CryptoAsset.user_id == user_id).all()

    portfolio = []
    total_value = 0

    for asset in assets:
        value = asset.quantity * asset.price
        total_value += value

        portfolio.append({
            "id": asset.id,
            "name": asset.name,
            "symbol": asset.symbol,
            "quantity": asset.quantity,
            "price": asset.price,
            "value": value
        })

    return {
        "assets": portfolio,
        "total_value": total_value
    }


# DELETE ASSET
@router.delete("/{asset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    asset = db.query(CryptoAsset).filter(
        CryptoAsset.id == asset_id,
        CryptoAsset.user_id == user_id
    ).first()

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    db.delete(asset)
    db.commit()
