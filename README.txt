================================================================================
THU THẬP BỘ DỮ LIỆU NGÔN NGỮ KÝ HIỆU VIỆT NAM (VSL) BẰNG GĂNG TAY THÔNG MINH
================================================================================

MÔ TẢ DỰ ÁN
------------
Dự án này tập trung vào việc phát triển một hệ thống nhận diện ngôn ngữ ký hiệu Việt Nam (VSL) sử dụng dữ liệu cảm biến từ găng tay thông minh tích hợp 6 cảm biến MPU6050. 
Thu thập dữ liệu khi người dùng thực hiện ngôn ngữ ký hiệu tiếng Việt. Bộ dữ liệu này được dùng để huấn luyện mô hình máy học để nhận dạng được ngôn ngữ ký hiệu, hỗ trợ cho người khuyết tật giao tiếp với người bình thường.  
Sau đó tiền xử lý và huấn luyện bằng các mô hình học sâu (CNN, LSTM, CNN-LSTM) trên Google Colab. Mục tiêu là triển khai mô hình trên ESP32 để nhận diện thời gian thực.

TÍNH NĂNG NỔI BẬT
-----------------
- Thu thập và tiền xử lý dữ liệu từ 6 MPU6050.
- Tăng cường dữ liệu để cải thiện hiệu suất mô hình.
- Xây dựng và so sánh các mô hình: CNN, LSTM, CNN-LSTM.
- Triển khai mô hình trên ESP32 kết hợp với web server cho ứng dụng thực tế.
- Hỗ trợ âm thanh phản hồi ký hiệu nhận diện (sử dụng gTTS).

TRẠNG THÁI DỰ ÁN
----------------
- HIỆN TẠI: Đang phát triển (hoàn thiện bộ dữ liệu và triển khai thực tế).
- PHIÊN BẢN: v1.0 (cập nhật ngày 10/08/2025).

TÁC GIẢ
-------
- Tên: Huỳnh Quang Huy
- Email: huynhquanghuyhs@gmail.com
- Trường: Trường Đại học Kiên Giang
