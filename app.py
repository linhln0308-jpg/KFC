import streamlit as st
import google.generativeai as genai

# Cấu hình API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🍔 KFC Food Advisor")
st.write("Nhập các thành phần bạn bị dị ứng, tôi sẽ gợi ý món ăn an toàn cho bạn!")

# Nhập danh sách dị ứng
allergies = st.text_input("Các thành phần bạn bị dị ứng (ví dụ: đậu phộng, tôm, hải sản):")

if st.button("Gợi ý món ăn"):
    if allergies:
        prompt = f"""
        Bạn là chuyên gia tư vấn thực phẩm của KFC. 
        Người dùng bị dị ứng với các thành phần sau: {allergies}.
        Hãy gợi ý cho họ các món ăn trong thực đơn KFC mà họ có thể ăn an toàn. 
        Nếu không có món nào an toàn, hãy cảnh báo họ. 
        Giải thích ngắn gọn lý do tại sao món đó an toàn.
        """
        
        with st.spinner('Đang tìm món ăn phù hợp cho bạn...'):
            response = model.generate_content(prompt)
            st.success("Dưới đây là gợi ý dành cho bạn:")
            st.write(response.text)
    else:
        st.warning("Vui lòng nhập món bạn bị dị ứng trước nhé!")
  
