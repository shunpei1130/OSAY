# AuthEssay デモ版の利用方法

このリポジトリには、学生のレポートを自動で評価するサービスのプロトタイプが含まれています。営業先でのデモ展示など、インターネット接続のない環境でも動作させられるよう、AI への問い合わせを行わずに定型の質問を返す **デモモード** を用意しています。

## 前提条件
- Python 3.11 以降
- Node.js 20 以降

## セットアップ手順

1. 依存パッケージのインストール
   ```bash
   pip install -r backend/requirements.txt
   cd frontend && npm install
   ```
2. 必要に応じて OpenAI の API キーを設定します（通常モードで動かす場合）。デモモードで動かす場合は `DEMO_MODE=1` を設定してください。
   ```bash
   export OPENAI_API_KEY=your-key      # 通常モードの場合
   export DEMO_MODE=1                  # デモモードの場合
   ```
3. バックエンドの起動
   ```bash
   uvicorn app.main:app --reload --app-dir backend
   ```
4. フロントエンドのビルドと起動
   ```bash
   cd frontend
   npm run build       # 一度だけ実行
   npm start           # localhost:3000 でサービスが立ち上がります
   ```

ブラウザで `http://localhost:3000` にアクセスすると、ログイン画面が表示されます。ユーザー名を入力してログインし、レポートの投稿、質問への回答、採点結果の確認まで一連の流れを体験できます。教師用のダッシュボードは `/dashboard` で確認できます。

保存されたデータは `backend/app.db` に SQLite 形式で格納されます。
