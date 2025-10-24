# 🐍 Hướng Dẫn Sử Dụng Script Python

## 📋 Tổng Quan

Tôi đã tạo **2 script Python** để hỗ trợ bạn quản lý ảnh cho website:

1. **`create_placeholders.py`** - Script quản lý ảnh cơ bản
2. **`download_images_advanced.py`** - Script tải ảnh tự động từ website

## 🛠️ Script 1: create_placeholders.py

### Chức năng:
- ✅ Tạo placeholder ảnh
- ✅ Kiểm tra trạng thái ảnh
- ✅ Sao lưu ảnh hiện tại
- ✅ Hiển thị hướng dẫn

### Cách sử dụng:

#### 1. Chạy cơ bản:
```bash
python create_placeholders.py
```
**Kết quả**: Tạo placeholder + kiểm tra trạng thái

#### 2. Kiểm tra trạng thái ảnh:
```bash
python create_placeholders.py --check
```
**Kết quả**: Hiển thị danh sách ảnh đã có/placeholder

#### 3. Sao lưu ảnh:
```bash
python create_placeholders.py --backup
```
**Kết quả**: Tạo thư mục backup với timestamp

#### 4. Xem hướng dẫn:
```bash
python create_placeholders.py --help
```
**Kết quả**: Hiển thị tất cả lệnh có thể dùng

### Ví dụ output:
```
============================================================
SCRIPT QUAN LY ANH WEBSITE DIEN LANH
============================================================
Tao anh placeholder...
Tao placeholder: images/banner/hero-bg.jpg
Tao placeholder: images/banner/about-us.jpg
...

==================================================
KIEM TRA TRANG THAI ANH
==================================================
📝 images/banner/hero-bg.jpg - Placeholder (81 bytes)
📝 images/banner/about-us.jpg - Placeholder (81 bytes)
✅ images/services/service-air-conditioner.jpg - Anh that (45,231 bytes)
...

📊 TONG KET:
   - Anh that: 5
   - Placeholder: 17
   - Tong cong: 22
```

## 🚀 Script 2: download_images_advanced.py

### Chức năng:
- ✅ Tự động tải ảnh từ website gốc
- ✅ Phân tích trang web để tìm ảnh
- ✅ Mapping thông minh ảnh với keywords
- ✅ Tải ảnh phù hợp nhất cho từng vị trí

### Cách sử dụng:

#### Chạy script:
```bash
python download_images_advanced.py
```

### Cách hoạt động:
1. **Phân tích trang chủ**: Tìm tất cả ảnh trên https://suachuadienlanh247.vn/
2. **Mapping thông minh**: Dùng keywords để tìm ảnh phù hợp
3. **Tải ảnh**: Tải ảnh có điểm số cao nhất
4. **Lưu file**: Đặt tên file chính xác theo cấu trúc

### Ví dụ output:
```
============================================================
🖼️  SCRIPT TẢI ẢNH TỪ WEBSITE ĐIỆN LẠNH 247
============================================================
Đang phân tích trang: https://suachuadienlanh247.vn/
📸 Tìm thấy 15 ảnh trên trang chủ

🔍 Tìm ảnh cho: images/banner/hero-bg.jpg
🎯 Tìm thấy ảnh phù hợp (điểm: 3)
Đang tải: https://suachuadienlanh247.vn/wp-content/uploads/2024/01/hero-banner.jpg
✅ Đã tải: images/banner/hero-bg.jpg (45,231 bytes)

🔍 Tìm ảnh cho: images/services/service-air-conditioner.jpg
🎯 Tìm thấy ảnh phù hợp (điểm: 2)
Đang tải: https://suachuadienlanh247.vn/wp-content/uploads/2024/01/dieu-hoa.jpg
✅ Đã tải: images/services/service-air-conditioner.jpg (32,156 bytes)

✅ Hoàn thành! Đã tải 8 ảnh
```

## 📦 Cài Đặt Dependencies

### Nếu chưa có Python:
1. Tải Python từ: https://python.org
2. Cài đặt với tùy chọn "Add to PATH"

### Cài đặt thư viện cần thiết:
```bash
pip install requests beautifulsoup4
```

## 🎯 Workflow Khuyến Nghị

### Bước 1: Kiểm tra trạng thái hiện tại
```bash
python create_placeholders.py --check
```

### Bước 2: Sao lưu ảnh hiện tại (nếu có)
```bash
python create_placeholders.py --backup
```

### Bước 3: Tải ảnh tự động
```bash
python download_images_advanced.py
```

### Bước 4: Kiểm tra kết quả
```bash
python create_placeholders.py --check
```

### Bước 5: Tải ảnh thủ công (nếu cần)
- Xem file `THAY_ANH_NHANH.md`
- Tải ảnh còn thiếu từ website

## ⚠️ Lưu Ý Quan Trọng

### 1. Bản quyền:
- Script chỉ tải ảnh để tham khảo
- Đảm bảo bạn có quyền sử dụng ảnh
- Nên thay thế bằng ảnh riêng khi triển khai

### 2. Kết nối mạng:
- Cần kết nối internet để tải ảnh
- Script có timeout 15 giây cho mỗi ảnh
- Nếu mạng chậm, có thể tải thủ công

### 3. Lỗi thường gặp:
- **"Module not found"**: Cài đặt `pip install requests beautifulsoup4`
- **"Connection timeout"**: Kiểm tra kết nối mạng
- **"Permission denied"**: Chạy với quyền admin (Windows)

## 🔧 Tùy Chỉnh Script

### Thay đổi website nguồn:
Mở file `download_images_advanced.py`, tìm dòng:
```python
main_url = 'https://suachuadienlanh247.vn/'
```
Thay đổi URL thành website khác.

### Thêm ảnh mới:
Mở file `create_placeholders.py`, thêm vào danh sách `images_to_create`:
```python
'images/new-folder/new-image.jpg',
```

## 🆘 Xử Lý Lỗi

### Lỗi "requests not found":
```bash
pip install requests
```

### Lỗi "beautifulsoup4 not found":
```bash
pip install beautifulsoup4
```

### Script không tải được ảnh:
1. Kiểm tra kết nối internet
2. Thử tải ảnh thủ công
3. Kiểm tra website có thay đổi không

---

**Chúc bạn sử dụng script thành công! 🎉**
