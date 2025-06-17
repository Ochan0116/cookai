import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AIzaSyDm29JmSI5QwkAGkzteaR1a5FF0HK49AyM"])

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

st.title("🍳 AI 요리 추천기")
ingredients = st.text_input("재료를 쉼표(,)로 입력하세요:", placeholder="예: 계란, 김, 밥")

if st.button("추천받기") and ingredients.strip():
    with st.spinner("AI가 요리를 고민 중입니다..."):
        prompt = f"{ingredients}를 사용해서 만들 수 있는 간단한 요리 하나 추천해줘. 요리 이름과 간단한 설명도 알려줘."
        try:
            response = model.generate_content(prompt)
            st.success("🍽 요리 추천 결과")
            st.write(response.text)
        except Exception as e:
            st.error(f"오류 발생: {e}")
