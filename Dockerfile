FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Node.jsとnpmをインストール
RUN apt-get update && apt-get install -y \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をインストール
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# package.jsonをコピーしてnpm install
COPY package.json .
RUN npm install

# Tailwind CSSをビルド
COPY tailwind.config.js .
COPY static/css/input.css ./static/css/
RUN npm run build:css

# アプリケーションのコードをコピー
COPY . .