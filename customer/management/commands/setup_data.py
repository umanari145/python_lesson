from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = '都道府県マスタとテストデータを順番に実行'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('========================================'))
        self.stdout.write(self.style.WARNING('データセットアップを開始します'))
        self.stdout.write(self.style.WARNING('========================================\n'))
        
        # 1. 都道府県マスタデータを作成
        self.stdout.write(self.style.WARNING('[1/2] 都道府県マスタデータを作成中...'))
        try:
            call_command('create_prefecture_data')
            self.stdout.write(self.style.SUCCESS('✓ 都道府県マスタデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 都道府県マスタデータの作成に失敗しました: {e}'))
            return
        
        # 2. 顧客テストデータを作成
        self.stdout.write(self.style.WARNING('[2/2] 顧客テストデータを作成中...'))
        try:
            call_command('create_test_data')
            self.stdout.write(self.style.SUCCESS('✓ 顧客テストデータの作成が完了しました\n'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ 顧客テストデータの作成に失敗しました: {e}'))
            return
        
        # 完了メッセージ
        self.stdout.write(self.style.SUCCESS('========================================'))
        self.stdout.write(self.style.SUCCESS('すべてのセットアップが完了しました！'))
        self.stdout.write(self.style.SUCCESS('========================================'))

