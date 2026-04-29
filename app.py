# 1. 필수 라이브러리 설치
!pip install streamlit

# 2. app.py 파일 생성 (스트림릿 코드)
%%writefile app.py
import streamlit as st

st.title("✨ 아이동 문장 변환기")
st.write("아이의 문장을 입력하면 더 풍성한 표현으로 바꿔줍니다.")

text = st.text_input("아이의 문장을 입력하세요:", "학교 갔어.")

if st.button("변환하기"):
    # 여기에 LLM 연동 코드를 넣거나, 간단한 예시 출력을 만듭니다.
    result = f"업그레이드: {text} 그리고 친구랑 재미있게 놀았어."
    st.success(result)