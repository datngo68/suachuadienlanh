# Hướng Dẫn Thay Thế Ảnh

## 📸 Cách Lấy Ảnh Từ Website Gốc

### 1. Sử dụng ảnh từ suachuadienlanh247.vn:

**Cách 1: Tải ảnh trực tiếp**
1. Truy cập https://suachuadienlanh247.vn/
2. Click chuột phải vào ảnh cần tải
3. Chọn "Lưu hình ảnh thành..."
4. Lưu vào thư mục tương ứng

**Cách 2: Sử dụng công cụ tải ảnh**
- Sử dụng extension "Image Downloader" trên Chrome
- Hoặc dùng công cụ wget/curl để tải hàng loạt

### 2. Kích thước ảnh khuyến nghị:

- **Banner/Hero**: 1200x600px
- **Dịch vụ**: 400x300px  
- **Tin tức**: 600x400px
- **Đội ngũ**: 300x300px
- **Logo**: 200x100px

### 3. Định dạng ảnh:
- **JPG**: Cho ảnh có nhiều màu sắc
- **PNG**: Cho ảnh có nền trong suốt
- **WebP**: Định dạng hiện đại, nhẹ hơn

## 🗂️ Cấu Trúc Thư Mục Ảnh

```
images/
├── banner/
│   ├── hero-bg.jpg          # Ảnh nền hero section
│   └── about-us.jpg         # Ảnh về chúng tôi
├── services/
│   ├── service-air-conditioner.jpg
│   ├── service-washing-machine.jpg
│   ├── service-refrigerator.jpg
│   ├── service-water-heater.jpg
│   ├── service-induction-cooker.jpg
│   └── service-microwave.jpg
├── placeholder/
│   ├── news-1.jpg           # Ảnh tin tức 1
│   ├── news-2.jpg           # Ảnh tin tức 2
│   ├── news-3.jpg           # Ảnh tin tức 3
│   ├── news-featured.jpg    # Ảnh tin tức nổi bật
│   ├── team-1.jpg           # Ảnh đội ngũ 1
│   ├── team-2.jpg           # Ảnh đội ngũ 2
│   ├── team-3.jpg           # Ảnh đội ngũ 3
│   ├── about-company.jpg    # Ảnh công ty
│   ├── article-air-conditioner.jpg
│   ├── related-1.jpg
│   ├── related-2.jpg
│   └── related-3.jpg
└── logo.png                 # Logo công ty
```

## 🔧 Cách Thay Thế Ảnh

### 1. Thay ảnh banner:
```html
<!-- Trong index.html -->
<img src="images/banner/hero-bg.jpg" alt="Banner điện lạnh">
```

### 2. Thay ảnh dịch vụ:
```html
<!-- Trong dich-vu/sua-dieu-hoa.html -->
<img src="images/services/service-air-conditioner.jpg" alt="Sửa điều hòa">
```

### 3. Thay ảnh tin tức:
```html
<!-- Trong tin-tuc/index.html -->
<img src="images/placeholder/news-1.jpg" alt="Tin tức">
```

## ⚠️ Lưu Ý Quan Trọng

1. **Bản quyền**: Đảm bảo bạn có quyền sử dụng ảnh
2. **Tối ưu hóa**: Nén ảnh để tăng tốc độ tải
3. **Alt text**: Luôn thêm alt text cho SEO
4. **Responsive**: Ảnh phải hiển thị tốt trên mobile

## 🛠️ Công Cụ Hỗ Trợ

- **TinyPNG**: Nén ảnh online
- **Canva**: Tạo ảnh banner
- **Unsplash**: Ảnh miễn phí chất lượng cao
- **Pexels**: Ảnh stock miễn phí
