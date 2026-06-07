import streamlit as st
import google.generativeai as genai

# Cấu hình API key
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Lỗi cấu hình API: {e}")
