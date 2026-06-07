import streamlit as st
import google.generativeai as genai

# Cấu hình API key an toàn
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    st.title("KFC Nutrition Checker")
    user_input = st.text_input("Nhập món ăn bạn muốn kiểm tra:")
    
    if user_input:
        response = model.generate_content(f"Phân tích dinh dưỡng của món: {user_input}")
        st.write(response.text)
        
except KeyError:
    st.error("Lỗi: Chưa tìm thấy 'GOOGLE_API_KEY' trong phần Secrets. Vui lòng kiểm tra lại cấu hình!")
except Exception as e:
    st.error(f"Đã xảy ra lỗi: {e}")
