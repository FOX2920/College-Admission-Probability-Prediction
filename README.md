# Dự án Dự đoán Xác suất Trúng tuyển vào Trường Cao Đẳng

## Mô tả
Dự án này triển khai một ứng dụng web sử dụng Streamlit để dự đoán xác suất trúng tuyển của thí sinh vào một trường cao đẳng dựa trên các thông số như điểm GRE, điểm TOEFL, điểm trường đại học, SOP, LOR, CGPA và có kinh nghiệm nghiên cứu hay không.

## Cách cài đặt
1. Clone repository này:

    ```
    git clone https://github.com/your_username/your_project.git
    ```

2. Di chuyển vào thư mục dự án:

    ```
    cd your_project
    ```

3. Cài đặt các thư viện cần thiết từ file `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

## Cách sử dụng
1. Chạy ứng dụng bằng lệnh sau:

    ```
    streamlit run app.py
    ```

2. Truy cập địa chỉ được hiển thị trong terminal để mở ứng dụng trên trình duyệt.

3. Điền thông tin thí sinh vào các trường thông số.

4. Nhấn nút "Dự đoán" để xem xác suất trúng tuyển vào trường cao đẳng.

## Cấu trúc dự án
- **app.py**: Mã nguồn của ứng dụng Streamlit.
- **lru_model.pkl**: File chứa mô hình được huấn luyện để dự đoán xác suất trúng tuyển.
- **requirements.txt**: Danh sách các thư viện Python cần thiết cho dự án.
