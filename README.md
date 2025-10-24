# Website Điện Lạnh 247 - Dịch Vụ Sửa Chữa Điện Lạnh

Website tĩnh về dịch vụ sửa chữa điện lạnh chuyên nghiệp tại Hải Phòng. Được xây dựng bằng HTML/CSS/JavaScript thuần với thiết kế responsive và giao diện hiện đại.

## 🌟 Tính Năng

- **Responsive Design**: Tối ưu cho mọi thiết bị (desktop, tablet, mobile)
- **SEO Friendly**: Cấu trúc HTML semantic, meta tags đầy đủ
- **Fast Loading**: Tối ưu hóa tốc độ tải trang
- **Modern UI/UX**: Giao diện đẹp, dễ sử dụng
- **Cross-browser Compatible**: Tương thích với mọi trình duyệt

## 📁 Cấu Trúc Thư Mục

```
Webdienlanh/
├── index.html              # Trang chủ
├── gioi-thieu.html        # Trang giới thiệu
├── lien-he.html           # Trang liên hệ
├── dich-vu/               # Thư mục dịch vụ
│   ├── sua-dieu-hoa.html
│   ├── sua-may-giat.html
│   ├── sua-tu-lanh.html
│   ├── sua-binh-nong-lanh.html
│   ├── sua-bep-tu.html
│   └── sua-lo-vi-song.html
├── tin-tuc/               # Thư mục tin tức
│   ├── index.html         # Danh sách bài viết
│   └── bai-viet/          # Các bài viết chi tiết
│       └── huong-dan-tu-sua-dieu-hoa.html
├── css/                   # Thư mục CSS
│   ├── style.css          # CSS chính
│   └── responsive.css     # CSS responsive
├── js/                    # Thư mục JavaScript
│   └── main.js            # JavaScript chính
└── images/                # Thư mục hình ảnh
    ├── banner/            # Ảnh banner
    ├── services/          # Ảnh dịch vụ
    └── placeholder/       # Ảnh demo
```

## 🚀 Cách Sử Dụng

### 1. Mở Website
- Mở file `index.html` trong trình duyệt web
- Hoặc sử dụng local server (khuyến nghị)

### 2. Sử Dụng Local Server (Khuyến Nghị)
```bash
# Sử dụng Python
python -m http.server 8000

# Sử dụng Node.js (nếu có live-server)
npx live-server

# Sử dụng PHP
php -S localhost:8000
```

Sau đó truy cập: `http://localhost:8000`

## 🎨 Tùy Chỉnh Giao Diện

### Thay Đổi Màu Sắc
Chỉnh sửa file `css/style.css`:

```css
/* Màu chính */
:root {
    --primary-color: #0066cc;    /* Xanh dương chính */
    --secondary-color: #ff6b35;  /* Cam phụ */
    --text-color: #333;          /* Màu chữ */
    --bg-color: #fff;            /* Màu nền */
}
```

### Thay Đổi Font Chữ
```css
body {
    font-family: 'Roboto', 'Open Sans', Arial, sans-serif;
}
```

### Thay Đổi Logo
Thay thế nội dung trong class `.logo`:
```html
<div class="logo">
    <i class="fas fa-tools"></i>
    Tên Công Ty Của Bạn
</div>
```

## 📝 Cập Nhật Nội Dung

### 1. Thông Tin Liên Hệ
Tìm và thay thế trong tất cả file HTML:

```html
<!-- Thay đổi số điện thoại -->
<a href="tel:0336288248">033.6288.248</a>

<!-- Thay đổi email -->
<a href="mailto:suachuadienlanh247vn@gmail.com">suachuadienlanh247vn@gmail.com</a>

<!-- Thay đổi địa chỉ -->
<p>52 Lê Thánh Tông, Ngô Quyền, Hải Phòng</p>
```

### 2. Thông Tin Công Ty
Chỉnh sửa file `gioi-thieu.html`:
- Tên công ty
- Lịch sử hình thành
- Đội ngũ nhân viên
- Giá trị cốt lõi

### 3. Dịch Vụ
Chỉnh sửa các file trong thư mục `dich-vu/`:
- Mô tả dịch vụ
- Giá cả
- Quy trình sửa chữa
- Lỗi thường gặp

### 4. Tin Tức
Thêm bài viết mới trong thư mục `tin-tuc/bai-viet/`:
1. Tạo file HTML mới
2. Copy cấu trúc từ file mẫu
3. Cập nhật nội dung
4. Thêm link vào `tin-tuc/index.html`

### 5. Hình Ảnh
Thay thế ảnh trong thư mục `images/`:
- **Banner**: Kích thước khuyến nghị 1200x600px
- **Dịch vụ**: Kích thước khuyến nghị 400x300px
- **Tin tức**: Kích thước khuyến nghị 600x400px
- **Đội ngũ**: Kích thước khuyến nghị 300x300px

## 🔧 Tùy Chỉnh Nâng Cao

### 1. Thêm Trang Mới
1. Tạo file HTML mới
2. Copy cấu trúc từ file mẫu
3. Cập nhật navigation menu
4. Thêm CSS nếu cần

### 2. Thêm Tính Năng JavaScript
Chỉnh sửa file `js/main.js`:
- Form validation
- Animation effects
- Interactive features

### 3. Tối Ưu SEO
Cập nhật meta tags trong `<head>`:
```html
<title>Tiêu đề trang</title>
<meta name="description" content="Mô tả trang">
<meta name="keywords" content="từ khóa">
```

## 📱 Responsive Breakpoints

```css
/* Desktop */
@media (min-width: 1200px) { }

/* Laptop */
@media (max-width: 1199px) { }

/* Tablet */
@media (max-width: 991px) { }

/* Mobile Large */
@media (max-width: 767px) { }

/* Mobile Small */
@media (max-width: 575px) { }
```

## 🌐 Triển Khai Website

### 1. Hosting Tĩnh
- **GitHub Pages**: Miễn phí, dễ sử dụng
- **Netlify**: Miễn phí, tự động deploy
- **Vercel**: Miễn phí, tốc độ cao

### 2. Hosting Thương Mại
- **Hostinger**: Giá rẻ, dễ sử dụng
- **GoDaddy**: Phổ biến, hỗ trợ tốt
- **Namecheap**: Giá cả hợp lý

### 3. Cấu Hình Domain
1. Mua domain
2. Cấu hình DNS
3. Upload files lên hosting
4. Cấu hình SSL certificate

## 🛠️ Công Cụ Hỗ Trợ

### 1. Code Editor
- **Visual Studio Code**: Khuyến nghị
- **Sublime Text**: Nhẹ, nhanh
- **Atom**: Miễn phí, nhiều plugin

### 2. Browser DevTools
- **Chrome DevTools**: F12
- **Firefox Developer Tools**: F12
- **Safari Web Inspector**: Cmd+Option+I

### 3. Testing Tools
- **Google PageSpeed Insights**: Kiểm tra tốc độ
- **GTmetrix**: Phân tích hiệu suất
- **Mobile-Friendly Test**: Kiểm tra mobile

## 📞 Hỗ Trợ

Nếu gặp vấn đề trong quá trình sử dụng:

1. **Kiểm tra Console**: Mở DevTools (F12) → Console
2. **Kiểm tra Network**: DevTools → Network
3. **Kiểm tra Responsive**: DevTools → Toggle device toolbar
4. **Kiểm tra CSS**: DevTools → Elements → Styles

## 📄 License

Website này được tạo ra cho mục đích thương mại. Bạn có thể:
- ✅ Sử dụng cho dự án cá nhân/thương mại
- ✅ Tùy chỉnh theo nhu cầu
- ✅ Phân phối cho khách hàng
- ❌ Bán lại dưới dạng template

## 🔄 Cập Nhật

### Version 1.0 (Hiện tại)
- ✅ Trang chủ hoàn chỉnh
- ✅ 6 trang dịch vụ
- ✅ Trang tin tức + bài viết mẫu
- ✅ Trang giới thiệu
- ✅ Trang liên hệ
- ✅ Responsive design
- ✅ JavaScript tương tác

### Kế Hoạch Tương Lai
- 🔄 Thêm blog system
- 🔄 Tích hợp Google Analytics
- 🔄 Thêm form liên hệ thật
- 🔄 Tối ưu SEO nâng cao
- 🔄 Thêm dark mode

---

**Chúc bạn sử dụng website thành công! 🎉**

Nếu cần hỗ trợ thêm, vui lòng liên hệ qua email hoặc tạo issue trên repository.
