import streamlit as st
import google.generativeai as genai

# Sửa thành dòng này:
genai.configure(api_key=st.secrets["AQ.Ab8RN6LFupkZgqJP5r01MLQg03f1yCquuleGdZSOhgiAVXZDzw"])

# Phần model giữ nguyên:
model = genai.GenerativeModel("gemini-1.5-flash")
