# Django 顧客管理システム - セットアップガイド

Django + Tailwind CSS + PostgreSQL + Dockerによる顧客管理システムです。

## 🚀 クイックスタート

### 1. Dockerコンテナの起動

```bash
# コンテナのビルドと起動
docker compose build
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
### webの起動

```bash
docker exec -it django_app bash
# migration
python manage.py migrate
# webサーバーの起動
python manage.py runserver  0:8000
```

スーパーユーザーの作成
```bash
python manage.py createsuperuser

Username: root
Email address: root@gmail.com
password pa$$w0rd#
```

個別プロジェクトの追加(初期設定と個別のモデルの２パターンある)
```bash
python manage.py startapp customer
```