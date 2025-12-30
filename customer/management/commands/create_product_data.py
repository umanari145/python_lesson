from django.core.management.base import BaseCommand
from customer.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = '商品マスタデータを作成'

    def handle(self, *args, **options):
        # 既存データを削除
        deleted_count = Product.objects.count()
        Product.objects.all().delete()
        self.stdout.write(f'既存商品データ{deleted_count}件を削除しました')
        
        # 商品データ
        products_data = [
            ('P001', 'ノートPC', 150000, 'ハイスペックノートパソコン'),
            ('P002', 'デスクトップPC', 180000, 'ゲーミングデスクトップ'),
            ('P003', 'マウス', 3000, 'ワイヤレスマウス'),
            ('P004', 'キーボード', 8000, 'メカニカルキーボード'),
            ('P005', 'モニター', 45000, '27インチ4Kモニター'),
            ('P006', 'Webカメラ', 12000, 'Full HD Webカメラ'),
            ('P007', 'ヘッドセット', 9000, 'ゲーミングヘッドセット'),
            ('P008', 'スピーカー', 15000, 'Bluetoothスピーカー'),
            ('P009', 'USBメモリ', 2000, '32GB USBメモリ'),
            ('P010', '外付けHDD', 15000, '2TB 外付けHDD'),
            ('P011', 'SSD', 12000, '1TB SSD'),
            ('P012', 'プリンター', 35000, '複合機プリンター'),
            ('P013', 'スキャナー', 28000, 'ドキュメントスキャナー'),
            ('P014', 'タブレット', 60000, '10インチタブレット'),
            ('P015', 'スマートフォン', 90000, '最新スマートフォン'),
            ('P016', '充電器', 3500, '急速充電器'),
            ('P017', 'USBケーブル', 1500, 'Type-C USBケーブル'),
            ('P018', 'モバイルバッテリー', 8000, '20000mAh モバイルバッテリー'),
            ('P019', 'ルーター', 12000, 'Wi-Fi 6 ルーター'),
            ('P020', 'LANケーブル', 800, 'Cat6 LANケーブル'),
        ]
        
        # 商品オブジェクトを作成
        products = []
        for product_code, name, price, description in products_data:
            product = Product(
                product_code=product_code,
                name=name,
                unit_price=Decimal(str(price)),
                description=description
            )
            products.append(product)
        
        # 一括作成
        Product.objects.bulk_create(products)
        
        self.stdout.write(self.style.SUCCESS(f'商品マスタデータを{len(products)}件作成しました'))

