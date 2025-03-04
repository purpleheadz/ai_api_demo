# OpenAI API デモアプリ

Streamlitを使用したOpenAI APIのデモアプリケーションです。テキスト生成AIモデルに質問を送信し、回答を取得できます。

## 機能

- OpenAI APIを使用したAIとの対話
- 複数のモデル選択（GPT-3.5 Turbo、GPT-4、GPT-4o）
- Temperatureパラメータの調整
- トークン使用量の表示

## インストール方法

1. リポジトリをクローンする
```bash
git clone https://github.com/yourusername/ai_api_demo.git
cd ai_api_demo
```

2. 必要なパッケージをインストールする
```bash
pip install streamlit openai
```

## 使用方法

1. アプリケーションを起動する
```bash
streamlit run app.py
```

2. ブラウザで表示されるアプリにOpenAI APIキーを入力する
3. 使用するモデルを選択する
4. 質問を入力して「送信」ボタンをクリックする

## 注意事項

- OpenAI APIキーは[OpenAIのウェブサイト](https://platform.openai.com/)で取得できます
- APIキーは公開しないように注意してください

## ライセンス

MITライセンス