import streamlit as st
import google.generativeai as genai

# Gọi trực tiếp từ secrets
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Sử dụng model flash mới nhất
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("KFC Nutrition Checker")
user_input = st.text_input("Nhập món ăn:")

if user_input:
    response = model.generate_content(f"Phân tích dinh dưỡng món: {user_input}")
    st.write(response.text)
  
