# Django 顧客管理システム - セットアップガイド

Django + Tailwind CSS + PostgreSQL + Dockerによる顧客管理システムです。

## 🚀 クイックスタート

### 1. Dockerコンテナの起動

```bash
# コンテナのビルドと起動
docker compose build
docker compose up -d
```

プロジェクト開始
```bash
docker compose run --rm web django-admin startproject config .
```


### 各パーツの意味
1.docker compose run
- Docker Composeで定義されたサービス内でコマンドを実行します

2.--rm
- コマンド実行後、作成された一時コンテナを自動的に削除します
- クリーンアップを自動化するオプション

3.web
- docker-compose.ymlで定義されているwebサービスを使用します
- このサービスのコンテナ内でコマンドが実行されます

4.django-admin startproject config .
- django-admin startproject: Djangoの新規プロジェクトを作成するコマンド
- config: プロジェクト名（設定ディレクトリの名前）
- .: 現在のディレクトリ（/app）に直接作成（サブディレクトリを作らない）
- .を付けると: /app/config/ と /app/manage.py が作成される

### psqlへのログイン

DBへのログイン
```bash
docker exec -it django_db bash 

psql -U postgres

postgres=# 
```
### webの起動(docker-composeでやっていることの説明)

```bash
docker exec -it django_app bash
# migration
python manage.py migrate
# webサーバーの起動
python manage.py runserver  0:8000
```

#### スーパーユーザーの作成(初期のコマンドで作らない場合はこのようにして作る)
```bash
docker exec -it django_app bash
python manage.py createsuperuser
Username: root
Email address: root@gmail.com
password pa$$w0rd#
```

個別プロジェクトの追加(初期設定と個別のモデルの２パターンある)
```bash
python manage.py startapp customer
```


#### migration関連
migrationファイルの作成
modelから自動的に作られる
```bash
docker-compose exec web python manage.py makemigrations
```

migrationの実行
```bash
docker-compose exec web python manage.py migrate
```

テストデータ投入
```bash
# 個別投入
docker-compose exec web python manage.py create_test_data
# 全実行
docker-compose exec web python manage.py setup_data
```

ロールバック
```bash
# 全ロールバック
docker-compose exec web python manage.py migrate customer zero
# customerアプリの0001_initialに戻る
docker-compose exec web python manage.py migrate customer 0001_initial
```

#### Tailwind CSSのセットアップ

```bash
# Node.jsの依存関係をインストール
docker compose exec web npm install

# Tailwind CSSをビルド
docker compose exec web npm run build:css

# 開発時は監視モードで自動ビルド
docker compose exec web npm run watch:css
```

## 📊 機能一覧

### 顧客管理機能
- **一覧表示**: `/customers/index/`
  - ページネーション対応
  - チェックボックスで複数選択削除
  - 会員Noクリックで編集画面へ
- **新規登録**: `/customers/create/`
  - バリデーション付きフォーム
  - 会員番号の重複チェック
- **編集**: `/customers/edit/<id>/`
- **削除**: 複数選択対応

### 売上管理機能
- **一覧表示**: `/customers/sales/`
  - 月別売上集計（直近12ヶ月）
  - 顧客別売上ランキング（上位10件）
  - ページネーション対応
- **新規登録**: `/customers/sales/create/`
  - 顧客選択、商品名、数量、単価入力
  - 金額は自動計算
- **編集**: `/customers/sales/edit/<id>/`
- **削除**: 複数選択対応

### データモデル

#### Customer（顧客）
- customer_no: 会員番号
- name: 名前
- registered_date: 登録日
- pref: 都道府県（外部キー）

#### Sales（売上）
- customer: 顧客（外部キー）
- sale_date: 売上日
- product_name: 商品名
- quantity: 数量
- unit_price: 単価
- amount: 金額（自動計算）

#### Prefecture（都道府県）
- code: 都道府県コード（1〜47）
- name: 都道府県名