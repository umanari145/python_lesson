"""
ビューパッケージ

各ビューを別ファイルに分離して管理します。
外部からは従来通り `from customer.views import list_view` のようにインポート可能です。
"""

from .customer import (
    list_view,
    create_view,
    update_view,
    delete_view,
)

from .sales import (
    list_view as sales_list_view,
    create_view as sales_create_view,
    update_view as sales_update_view,
    delete_view as sales_delete_view,
)

__all__ = [
    # 顧客関連
    'list_view',
    'create_view',
    'update_view',
    'delete_view',
    # 売上関連
    'sales_list_view',
    'sales_create_view',
    'sales_update_view',
    'sales_delete_view',
]

