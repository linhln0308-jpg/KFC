import streamlit as st
import google.generativeai as genai

# Sửa thành dòng này:
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Phần model giữ nguyên:
model = genai.GenerativeModel("gemini-1.5-flash")
