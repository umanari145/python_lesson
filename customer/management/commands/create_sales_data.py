from django.core.management.base import BaseCommand
from customer.models import Customer, Product, Sales
from decimal import Decimal
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = '売上テストデータを作成'

    def handle(self, *args, **options):
        # 既存データを削除
        deleted_count = Sales.objects.count()
        Sales.objects.all().delete()
        self.stdout.write(f'既存売上データ{deleted_count}件を削除しました')
        
        # 顧客を取得
        customers = list(Customer.objects.all())
        
        if not customers:
            self.stdout.write(self.style.ERROR('顧客データが存在しません。先に顧客データを作成してください。'))
            return
        
        # 商品を取得
        products = list(Product.objects.all())
        
        if not products:
            self.stdout.write(self.style.ERROR('商品データが存在しません。先に商品データを作成してください。'))
            return
        
        sales_list = []
        
        # 過去12ヶ月分の売上データを生成
        today = date.today()
        
        for customer in customers:
            # 各顧客につき、ランダムに3〜10件の購入履歴を作成
            num_purchases = random.randint(3, 10)
            
            for _ in range(num_purchases):
                # ランダムな日付（過去12ヶ月以内）
                days_ago = random.randint(0, 365)
                sale_date = today - timedelta(days=days_ago)
                
                # ランダムな商品を選択
                product = random.choice(products)
                
                # 数量（1〜5個）
                quantity = random.randint(1, 5)
                
                # 単価（標準価格の±20%の範囲でランダム）
                price_variation = random.uniform(0.8, 1.2)
                unit_price = product.standard_price * Decimal(str(price_variation))
                # 小数点第2位で四捨五入
                unit_price = unit_price.quantize(Decimal('0.01'))
                
                sale = Sales(
                    customer=customer,
                    product=product,
                    sale_date=sale_date,
                    quantity=quantity,
                    unit_price=unit_price,
                    amount=quantity * unit_price
                )
                sales_list.append(sale)
        
        # 一括作成
        Sales.objects.bulk_create(sales_list)
        
        self.stdout.write(self.style.SUCCESS(f'売上テストデータを{len(sales_list)}件作成しました'))
        
        # 統計情報を表示
        total_amount = sum(sale.quantity * sale.unit_price for sale in sales_list)
        self.stdout.write(f'総売上金額: ¥{total_amount:,.0f}')

