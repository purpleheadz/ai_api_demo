import streamlit as st
import openai
import os

# 設定
st.set_page_config(page_title="OpenAI API デモ", layout="wide")

# サイドバー - API設定
st.sidebar.title("設定")
api_key = st.sidebar.text_input("OpenAI API キー", type="password")
model = st.sidebar.selectbox(
    "モデル",
    ["gpt-3.5-turbo", "gpt-4", "gpt-4o"]
)

# メイン画面
st.title("OpenAI API デモアプリ")

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
            # APIキーの設定
            client = openai.OpenAI(api_key=api_key)
            
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
    1. サイドバーにOpenAI APIキーを入力してください
    2. 使用するモデルを選択してください
    3. 質問を入力し、送信ボタンをクリックしてください
    
    注意: APIキーは安全に保管され、このアプリ内でのみ使用されます。
    """)