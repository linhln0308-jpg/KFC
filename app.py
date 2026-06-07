import streamlit as st
import google.generativeai as genai

# Cấu hình API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("KFC Nutrition Checker")
user_input = st.text_input("Nhập món ăn bạn muốn kiểm tra:")

if user_input:
    try:
        response = model.generate_content(f"Phân tích dinh dưỡng của món: {user_input}")
        st.write(response.text)
    except Exception as e:
        st.error(f"Lỗi khi gọi AI: {e}")
