import logging

import boto3
from fastapi import APIRouter, HTTPException

from app.settings import DATABASE

logger = logging.getLogger(__name__)

router = APIRouter(redirect_slashes=False)


@router.get("/food")
def get_clubs(product: str):
    table = DATABASE.Table('Food')

    try:
        product = table.get_item(Key={'product': product})
        if not product.get('Item'):
            raise HTTPException(status_code=404, detail="Product not found")

    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500)
    else:
        return product['Item']
