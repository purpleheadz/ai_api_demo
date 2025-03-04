# AI API デモアプリ

Streamlitを使用したAI APIのデモアプリケーションです。OpenAIおよびOpenAI互換APIを使用して、テキスト生成AIモデルに質問を送信し、回答を取得できます。

## 機能

- OpenAI APIおよびOpenAI互換APIを使用したAIとの対話
- カスタムAPI Base URLの設定
- 複数のモデル選択（GPT、Claude、LLaMAなど）
- カスタムモデル名の指定
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

2. ブラウザで表示されるアプリでAPI種類を選択する（OpenAIまたはOpenAI互換）
3. APIキーを入力する
4. OpenAI互換APIを選択した場合は、API Base URLも入力する
5. 使用するモデルを選択する（またはカスタムモデル名を入力）
6. 質問を入力して「送信」ボタンをクリックする

## 対応API

以下のようなOpenAI互換APIに対応しています：

- [OpenAI API](https://platform.openai.com/)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Together AI](https://www.together.ai/)
- [Groq](https://console.groq.com/)
- その他のOpenAI互換API

## 注意事項

- 各サービスのAPIキーは各プロバイダーから取得してください
- APIキーは公開しないように注意してください
- 各APIプロバイダーの利用規約に従ってご利用ください

## ライセンス

MITライセンス