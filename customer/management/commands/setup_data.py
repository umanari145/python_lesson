from django.core.management.base import BaseCommand
from django.core.management import call_command
from customer.models import Sales, Customer, Product, Prefecture

class Command(BaseCommand):
    help = '都道府県マスタ、商品マスタ、顧客データ、売上データを順番に作成'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('========================================'))
        self.stdout.write(self.style.WARNING('データセットアップを開始します'))
        self.stdout.write(self.style.WARNING('========================================\n'))
        
        # 0. 既存データを全削除
        self.stdout.write(self.style.WARNING('[0/4] 既存データを削除中...'))
        try:
            # 外部キーの参照順に削除（参照される側から削除）
            sales_count = Sales.objects.count()
            Sales.objects.all().delete()
            self.stdout.write(f'  - 売上データ: {sales_count}件を削除')
            
            customer_count = Customer.objects.count()
            Customer.objects.all().delete()
            self.stdout.write(f'  - 顧客データ: {customer_count}件を削除')
            
            product_count = Product.objects.count()
            Product.objects.all().delete()
            self.stdout.write(f'  - 商品データ: {product_count}件を削除')
            
            prefecture_count = Prefecture.objects.count()
            Prefecture.objects.all().delete()
            self.stdout.write(f'  - 都道府県データ: {prefecture_count}件を削除')
            
            total_count = sales_count + customer_count + product_count + prefecture_count
            self.stdout.write(self.style.SUCCESS(f'✓ 既存データ合計{total_count}件を削除しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ データ削除に失敗しました: {e}'))
            return
        
        # 1. 都道府県マスタデータを作成
        self.stdout.write(self.style.WARNING('[1/4] 都道府県マスタデータを作成中...'))
        try:
            call_command('create_prefecture_data')
            self.stdout.write(self.style.SUCCESS('✓ 都道府県マスタデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 都道府県マスタデータの作成に失敗しました: {e}'))
            return
        
        # 2. 商品マスタデータを作成
        self.stdout.write(self.style.WARNING('[2/4] 商品マスタデータを作成中...'))
        try:
            call_command('create_product_data')
            self.stdout.write(self.style.SUCCESS('✓ 商品マスタデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 商品マスタデータの作成に失敗しました: {e}'))
            return
        
        # 3. 顧客テストデータを作成
        self.stdout.write(self.style.WARNING('[3/4] 顧客テストデータを作成中...'))
        try:
            call_command('create_test_data')
            self.stdout.write(self.style.SUCCESS('✓ 顧客テストデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 顧客テストデータの作成に失敗しました: {e}'))
            return
        
        # 4. 売上テストデータを作成
        self.stdout.write(self.style.WARNING('[4/4] 売上テストデータを作成中...'))
        try:
            call_command('create_sales_data')
            self.stdout.write(self.style.SUCCESS('✓ 売上テストデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 売上テストデータの作成に失敗しました: {e}'))
            return
        
        # 完了メッセージ
        self.stdout.write(self.style.SUCCESS('========================================'))
        self.stdout.write(self.style.SUCCESS('すべてのセットアップが完了しました！'))
        self.stdout.write(self.style.SUCCESS('========================================'))

