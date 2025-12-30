"""
モデルパッケージ

各モデルを別ファイルに分離して管理します。
外部からは従来通り `from customer.models import Customer` のようにインポート可能です。
"""

from .prefecture import Prefecture
from .customer import Customer
from .product import Product
from .sales import Sales

__all__ = [
    'Prefecture',
    'Customer',
    'Product',
    'Sales',
]

