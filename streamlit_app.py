
import streamlit as st

st.title("👋 자기소개 페이지")

st.image("https://avatars.githubusercontent.com/u/99167854?v=4", width=150)

st.header("안녕하세요! 저는 김승욱입니다.")
st.subheader("수학교육과 23학번 04년생(23살) 입니다.")

st.markdown("""
**주요 소개:**
- ☕ 아메리카노를 좋아합니다.
- 🐱 고양이 영상을 자주 봅니다.
- 🎵 노래 듣는 걸 좋아합니다.
- 🍕 피자를 좋아합니다. 파인애플피자는 안먹습니다.
""")

st.info("궁금한 점이 있으면 언제든 연락 주세요!")
