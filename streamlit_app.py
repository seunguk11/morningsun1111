
import streamlit as st

st.set_page_config(page_title="큰 글자", layout="centered")

# 텍스트 입력
text = st.text_input("글자를 입력하세요:", placeholder="여기에 글자를 입력. . .")

# 큰 폰트로 표시
if text:
    st.markdown(f"<h1 style='text-align: center; font-size: 150px;'>{text}</h1>", unsafe_allow_html=True)
