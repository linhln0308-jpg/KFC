import streamlit as st
import pandas as pd
import google.generativeai as genai

# =========================
# CẤU HÌNH GEMINI API
# =========================
API_KEY = "AQ.Ab8RN6LFupkZgqJP5r01MLQg03f1yCquuleGdZSOhgiAVXZDzw"

genai.configure(api_key=API_KEY)

# Sử dụng model mới
model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# GIAO DIỆN
# =========================
st.set_page_config(
    page_title="KFC AI Nutrition Check",
    page_icon="🍗",
    layout="centered"
)

st.title("🍗 KFC AI Nutrition Check")
st.write("Kiểm tra dị ứng thực phẩm và nhận gợi ý món ăn an toàn.")

# =========================
# PHẦN 1: KHÁCH HÀNG
# =========================
st.subheader("👤 Kiểm tra cho khách hàng")

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTnb2_cjYGgrW4Htcv5Q-otaGvQpRlyCn5d8QiU9hu51W7sEFevrcVmTtZCXX2-W3LORltJNy1Hsk0N/pub?gid=747444077&single=true&output=csv"

try:
    df_cust = pd.read_csv(sheet_url)

    if "Name" not in df_cust.columns or "Allergies" not in df_cust.columns:
        st.error("File CSV phải có cột 'Name' và 'Allergies'")

    else:
        name = st.selectbox(
            "Chọn khách hàng",
            df_cust["Name"].tolist()
        )

        if st.button("Kiểm tra thông tin khách hàng"):
            allergy = df_cust.loc[
                df_cust["Name"] == name,
                "Allergies"
            ].values[0]

            prompt = f"""
            Bạn là chuyên gia dinh dưỡng.

            Khách hàng: {name}
            Dị ứng: {allergy}

            Hãy:
            1. Giải thích các thực phẩm cần tránh.
            2. Đề xuất các món KFC phù hợp.
            3. Cảnh báo các thành phần có thể gây dị ứng.
            4. Trình bày ngắn gọn bằng tiếng Việt.
            """

            with st.spinner("Đang phân tích..."):
                response = model.generate_content(prompt)
                st.success("Hoàn tất!")
                st.write(response.text)

except Exception as e:
    st.warning(
        f"Không thể đọc dữ liệu khách hàng.\n\nChi tiết lỗi: {e}"
    )

st.divider()

# =========================
# PHẦN 2: TRA CỨU MÓN ĂN
# =========================
st.subheader("🍔 Tra cứu nhanh theo món ăn")

food_input = st.text_input(
    "Nhập tên món ăn KFC",
    placeholder="Ví dụ: Gà Rán, Burger Tôm, Zinger Burger..."
)

allergy_input = st.text_input(
    "Dị ứng của bạn",
    placeholder="Ví dụ: đậu phộng, sữa, gluten, hải sản..."
)

if st.button("Đề xuất món thay thế"):
    if not food_input:
        st.error("Vui lòng nhập tên món ăn.")
    else:

        prompt = f"""
        Bạn là chuyên gia dinh dưỡng.

        Món ăn KFC: {food_input}
        Dị ứng của khách hàng: {allergy_input}

        Hãy:
        1. Phân tích nguy cơ dị ứng.
        2. Nêu các thành phần cần lưu ý.
        3. Đề xuất món thay thế an toàn hơn tại KFC.
        4. Trình bày dạng gạch đầu dòng.
        """

        with st.spinner("Đang phân tích..."):
            try:
                response = model.generate_content(prompt)
                st.success("Hoàn tất!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Lỗi Gemini API: {e}")

st.divider()

# =========================
# FOOTER
# =========================
st.caption("Powered by Google Gemini + Streamlit")