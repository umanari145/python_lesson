from django.core.management.base import BaseCommand
from customer.models import Customer
import csv
import os

class Command(BaseCommand):
    help = 'CSVファイルからテストデータを作成'

    def handle(self, *args, **options):
        # 既存データを削除
        deleted_count = Customer.objects.count()
        Customer.objects.all().delete()
        self.stdout.write(f'既存データ{deleted_count}件を削除しました')
        
        # CSVファイルのパス
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'fixtures',
            'test_customers.csv'
        )
        
        # CSVファイルを読み込み
        customers = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                customer = Customer(
                    customer_no=int(row['customer_no']),
                    name=row['name'],
                    registered_date=row['registered_date'],
                    pref=int(row['pref'])
                )
                customers.append(customer)
        
        # 一括作成
        Customer.objects.bulk_create(customers)
        
        self.stdout.write(f'テストデータを{len(customers)}件作成しました')