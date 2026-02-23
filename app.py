import streamlit as st
from google import genai

# --- 設定（セキュリティ対策版） ---
# st.secrets という機能を使って、外部から安全にAPIキーを読み込みます
API_KEY = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=API_KEY)

# --- 画面の見た目 ---
st.set_page_config(page_title="英語日記の添削くん", page_icon="📝")
st.title("📝 英語日記の添削くん")

user_input = st.text_input("ここに英文を入力してね", placeholder="I go to park yesterday.")

if st.button("先生に添削してもらう"):
    if user_input:
        with st.spinner("AI先生が考え中..."):
            try:
                response = client.models.generate_content(
                    model='gemini-flash-latest',
                    contents=f"英語の先生として、次の英文を添削し、日本語で1行アドバイスをください：'{user_input}'"
                )
                st.success("添削完了！")
                st.markdown("### 🌟 AI先生の回答")
                st.write(response.text)
            except Exception as e:
                st.error("エラーが発生しました。時間をおいて試してください。")
