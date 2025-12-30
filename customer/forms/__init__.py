"""
フォームパッケージ

各フォームを別ファイルに分離して管理します。
外部からは従来通り `from customer.forms import CustomerForm` のようにインポート可能です。
"""

from .customer import CustomerForm
from .sales import SalesForm

__all__ = [
    'CustomerForm',
    'SalesForm',
]

