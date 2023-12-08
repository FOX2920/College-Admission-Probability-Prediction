import streamlit as st
import os
import joblib
import numpy as np

# Load the Naive Bayes model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "lru_model.pkl")

# Load the CountVectorizer
model = joblib.load(model_path)

# Streamlit app
def main():
    # Tiêu đề ứng dụng
    st.title('Dự đoán Xác suất Trúng tuyển vào Trường Cao Đẳng')

    # Hiển thị bảng giải thích cho các từ viết tắt
    # Bảng giải thích các từ viết tắt
    st.sidebar.header('Bảng Giải Thích')
    st.sidebar.markdown('**GRE Score**: General Record Examination - Điểm kiểm tra tổng quát')
    st.sidebar.markdown('**TOEFL Score**: Test of English as a Foreign Language - Điểm kiểm tra Tiếng Anh như một Ngoại ngữ')
    st.sidebar.markdown('**SOP**: Statement of Purpose - Tuyên bố Mục tiêu')
    st.sidebar.markdown('**LOR**: Letter of Recommendation - Thư giới thiệu')
    st.sidebar.markdown('**CGPA**: Cumulative Grade Point Average - Điểm trung bình tích lũy')
    st.sidebar.markdown('**Research**: Có kinh nghiệm nghiên cứu hay không')

    # Form để nhập thông số thí sinh
    st.header('Thông số Thí sinh và Trường Cao Đẳng')
    gre_score = st.slider('GRE Score', 280, 340, 310)
    toefl_score = st.slider('TOEFL Score', 80, 120, 100)
    university_rating = st.slider('University Rating', 1, 5, 3)
    sop = st.slider('SOP', 1.0, 5.0, 3.5)
    lor = st.slider('LOR', 1.0, 5.0, 3.5)
    cgpa = st.slider('CGPA', 6.0, 10.0, 8.0)
    research = st.checkbox('Research', value=True)

    # Dự đoán xác suất trúng tuyển khi nhấn nút
    if st.button('Dự đoán'):
        input_data = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, int(research)]])
        admission_chance = model.predict(input_data)[0]
        st.subheader(f'Xác suất trúng tuyển: {admission_chance:.2%}')

if __name__ == "__main__":
    main()