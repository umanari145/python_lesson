FROM python:3.11-slim

# 環境変数の設定
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 作業ディレクトリの設定
WORKDIR /app

# システムパッケージのインストール
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージのインストール
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# ポートの公開
EXPOSE 8000

# 起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

