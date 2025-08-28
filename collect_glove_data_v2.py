import serial
import csv
import os
import time

# === Cấu hình ===
SERIAL_PORT = "COM3"  # Thay bằng cổng Serial thực tế
BAUD_RATE = 115200
DATA_DIR = 'sign_language_data'
DURATION = 7  # thời gian thu thập (giây)

# === Tạo thư mục chính nếu chưa có ===
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# === Lấy số mẫu tiếp theo ===
def get_next_sample_number(sign_dir):
    if not os.path.exists(sign_dir):
        os.makedirs(sign_dir)
        return 1
    existing_files = [f for f in os.listdir(sign_dir) if f.endswith('.csv')]
    if not existing_files:
        return 1
    max_number = max([int(f.split('_')[-1].split('.')[0]) for f in existing_files])
    return max_number + 1

# === Thu thập dữ liệu ===
def collect_sample(sign, sample_number):
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        ser.setDTR(False)
        ser.setRTS(False)
        time.sleep(1)
        ser.reset_input_buffer()

        # Đợi ESP32 gửi READY
        print("⏳ Đang chờ ESP32 khởi động...")
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if "READY" in line:
                print("✅ ESP32 đã sẵn sàng. Bắt đầu ghi dữ liệu...")
                break

        # Mở file CSV
        sign_dir = os.path.join(DATA_DIR, sign)
        filename = os.path.join(sign_dir, f'{sign}_{sample_number:03d}.csv')
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            header = ['Timestamp'] + [f'{sensor}_{axis}' for sensor in ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky', 'Wrist'] for axis in ['angleX', 'angleY']]
            writer.writerow(header)

            print(f"📦 Thu thập dữ liệu trong {DURATION} giây...")
            start_time = time.time()
            while time.time() - start_time < DURATION:
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if not line:
                        continue
                    if "Timestamp" in line:  # Bỏ qua dòng header
                        continue
                    data = line.split(',')
                    if len(data) == 13 and data[0].isdigit():
                        writer.writerow(data)
                        print(f"✅ Dữ liệu: {line}")
                    else:
                        print(f"⚠️ Dòng không hợp lệ: {line}")
                except Exception as e:
                    print(f"❌ Lỗi khi đọc: {e}")
                    continue

        ser.close()
        print(f"📁 Đã lưu mẫu vào: {filename}")

    except serial.SerialException as e:
        print(f"❌ Lỗi Serial: {e}")
        if 'ser' in locals() and ser.is_open:
            ser.close()


# === Giao diện người dùng ===
def main():
    while True:
        sign = input("\nNhập ký hiệu (hoặc 'e' để thoát): ").strip().upper()
        if sign == 'e':
            break
        if not sign:
            print("⚠️ Vui lòng nhập ký hiệu hợp lệ!")
            continue

        sign_dir = os.path.join(DATA_DIR, sign)
        sample_number = get_next_sample_number(sign_dir)
        input(f"👉 Chuẩn bị thực hiện ký hiệu '{sign}' (mẫu {sample_number}). Nhấn Enter để bắt đầu...")
        collect_sample(sign, sample_number)

if __name__ == "__main__":
    main()
