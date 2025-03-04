import streamlit as st
import openai
import os

# 設定
st.set_page_config(page_title="AI API デモ", layout="wide")

# サイドバー - API設定
st.sidebar.title("設定")
api_type = st.sidebar.radio("API種類", ["OpenAI", "OpenAI互換"])

# API設定
api_key = st.sidebar.text_input("APIキー", type="password")

# OpenAI互換APIの場合はベースURLを入力できるように
if api_type == "OpenAI互換":
    api_base = st.sidebar.text_input("API Base URL", placeholder="https://api.example.com/v1")
else:
    api_base = None

model = st.sidebar.selectbox(
    "モデル",
    ["gpt-3.5-turbo", "gpt-4", "gpt-4o", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "llama-2-70b", "custom"]
)

# カスタムモデル名入力
if model == "custom":
    custom_model = st.sidebar.text_input("カスタムモデル名")
    if custom_model:
        model = custom_model

# メイン画面
st.title("AI API デモアプリ")

# ユーザー入力
user_input = st.text_area("質問を入力してください:", height=150)
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

# 送信ボタン
if st.button("送信"):
    if not api_key:
        st.error("APIキーを入力してください")
    elif not user_input:
        st.error("質問を入力してください")
    else:
        try:
            # APIクライアントの設定
            if api_type == "OpenAI":
                client = openai.OpenAI(api_key=api_key)
            else:
                # OpenAI互換APIの場合
                if not api_base:
                    st.error("API Base URLを入力してください")
                    st.stop()
                client = openai.OpenAI(api_key=api_key, base_url=api_base)
            
            # プログレスバーの表示
            with st.spinner("回答を生成中..."):
                # APIリクエスト
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "あなたは役立つAIアシスタントです。"},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=temperature,
                )
                
                # 回答の表示
                st.subheader("回答:")
                st.write(response.choices[0].message.content)
                
                # 使用トークン数の表示
                st.info(f"使用トークン数: {response.usage.total_tokens} (プロンプト: {response.usage.prompt_tokens}, 生成: {response.usage.completion_tokens})")
                
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

# 使い方説明
with st.expander("使い方"):
    st.write("""
    1. サイドバーでAPI種類を選択してください（OpenAIまたはOpenAI互換API）
    2. APIキーを入力してください
    3. OpenAI互換APIを選択した場合は、API Base URLも入力してください
       - 例: https://api.anthropic.com/v1 (Anthropic Claude)
       - 例: https://api.together.xyz/v1 (Together AI)
       - 例: https://api.groq.com/openai/v1 (Groq)
    4. 使用するモデルを選択してください（または「custom」を選んでカスタムモデル名を入力）
    5. 質問を入力し、送信ボタンをクリックしてください
    
    注意: APIキーは安全に保管され、このアプリ内でのみ使用されます。
    """)