# ⚙️ Hướng Dẫn Cấu Hình Tập Trung

## 🎯 Tổng Quan

Tôi đã tạo **hệ thống cấu hình tập trung** để bạn có thể sửa thông tin liên hệ ở **1 nơi duy nhất** và nó sẽ tự động cập nhật toàn bộ website!

### ✅ **Đã Hoàn Thành:**

1. **📁 File cấu hình**: `js/config.js` - Chứa tất cả thông tin
2. **🔄 Auto-update**: Tự động cập nhật khi trang load
3. **📱 Responsive**: Hoạt động trên mọi thiết bị
4. **🎨 Data attributes**: Tích hợp với HTML hiện tại

## 📋 **Cách Sử Dụng**

### 🔧 **Sửa Thông Tin Liên Hệ:**

Mở file `js/config.js` và sửa thông tin trong phần `contact`:

```javascript
contact: {
    phone: "033.6288.248",        // Số điện thoại hiển thị
    phoneRaw: "0336288248",       // Số điện thoại không dấu chấm
    zalo: "033.6288.248",         // Số Zalo hiển thị
    zaloRaw: "0336288248",        // Số Zalo không dấu chấm
    email: "suachuadienlanh247vn@gmail.com",
    website: "suachuadienlanh247.vn"
}
```

### 🏢 **Sửa Địa Chỉ Các Cơ Sở:**

```javascript
addresses: [
    {
        name: "Cơ sở chính 1",
        address: "52 Lê Thánh Tông, Ngô Quyền, Hải Phòng",
        phone: "033.6288.248"
    },
    // Thêm cơ sở mới hoặc sửa cơ sở hiện tại
]
```

### 🌐 **Sửa Mạng Xã Hội:**

```javascript
social: {
    facebook: "https://facebook.com/your-page",  // Link Facebook thật
    youtube: "https://youtube.com/your-channel", // Link YouTube thật
    zalo: "https://zalo.me/0336288248"
}
```

### 🏷️ **Sửa Thông Tin Công Ty:**

```javascript
company: {
    name: "Sửa Chữa Điện Lạnh 247",
    fullName: "Dịch vụ sửa chữa điện lạnh 24/7",
    slogan: "Chi phí thấp - Đảm bảo kỹ thuật - Phục vụ tận tình"
}
```

## 🎯 **Ví Dụ Thực Tế**

### **Thay đổi số điện thoại:**

1. **Mở file**: `js/config.js`
2. **Tìm dòng**: `phone: "033.6288.248"`
3. **Sửa thành**: `phone: "0123.456.789"`
4. **Lưu file**
5. **Refresh website** - Tất cả số điện thoại sẽ tự động cập nhật!

### **Thêm cơ sở mới:**

```javascript
addresses: [
    // ... các cơ sở cũ ...
    {
        name: "Cơ sở 8",
        address: "123 Đường Mới, Quận Mới, Hải Phòng",
        phone: "033.6288.248"
    }
]
```

### **Cập nhật Facebook:**

```javascript
social: {
    facebook: "https://facebook.com/suachuadienlanh247", // Link thật
    // ... các mạng xã hội khác ...
}
```

## 📊 **Thông Tin Được Tự Động Cập Nhật**

### ✅ **Số điện thoại:**
- Footer tất cả trang
- Hotline hỗ trợ
- Link `tel:` tự động
- Button "Gọi ngay"

### ✅ **Email:**
- Footer tất cả trang
- Link `mailto:` tự động
- Form liên hệ

### ✅ **Zalo:**
- Floating button
- Social links
- Button "Chat Zalo"
- Link Zalo tự động

### ✅ **Website:**
- Footer tất cả trang
- Link website tự động

### ✅ **Địa chỉ:**
- Trang liên hệ
- Danh sách cơ sở
- Tự động tạo HTML

### ✅ **Mạng xã hội:**
- Facebook links
- YouTube links
- Zalo links

## 🔧 **Cách Hoạt Động**

### **1. Data Attributes:**
HTML sử dụng data attributes để nhận diện:
```html
<a href="tel:0336288248" data-phone>033.6288.248</a>
<span data-email>suachuadienlanh247vn@gmail.com</span>
<a href="#" data-facebook>Facebook</a>
```

### **2. JavaScript Auto-Update:**
```javascript
function updateContactInfo() {
    // Tìm tất cả elements có data-phone
    const phoneElements = document.querySelectorAll('[data-phone]');
    // Cập nhật nội dung và link
    phoneElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.contact.phone;
        el.href = `tel:${WEBSITE_CONFIG.contact.phoneRaw}`;
    });
}
```

### **3. Tự Động Chạy:**
- Chạy khi trang load
- Cập nhật tất cả elements
- Không cần thao tác thêm

## 📱 **Test Hệ Thống**

### **Bước 1: Sửa thông tin**
1. Mở `js/config.js`
2. Sửa số điện thoại: `phone: "0123.456.789"`
3. Lưu file

### **Bước 2: Kiểm tra kết quả**
1. Mở `index.html` trong trình duyệt
2. Refresh trang (F5)
3. Kiểm tra footer - số điện thoại đã thay đổi
4. Click vào số điện thoại - link `tel:` đã cập nhật

### **Bước 3: Kiểm tra tất cả trang**
1. Mở các trang khác (liên hệ, dịch vụ, tin tức)
2. Tất cả số điện thoại đều đã cập nhật
3. Floating Zalo button cũng đã cập nhật

## 🎉 **Lợi Ích**

### ✅ **Tiết kiệm thời gian:**
- Sửa 1 lần, cập nhật toàn bộ website
- Không cần tìm từng file HTML
- Không cần sửa thủ công

### ✅ **Tránh lỗi:**
- Không bị sót trang nào
- Đồng bộ 100% thông tin
- Tự động cập nhật link

### ✅ **Dễ bảo trì:**
- Tập trung 1 file cấu hình
- Dễ tìm và sửa
- Có comment hướng dẫn

### ✅ **Linh hoạt:**
- Thêm/sửa/xóa thông tin dễ dàng
- Hỗ trợ nhiều cơ sở
- Mở rộng dễ dàng

## 🚀 **Mở Rộng**

### **Thêm thông tin mới:**
1. Thêm vào `WEBSITE_CONFIG`
2. Thêm function cập nhật
3. Thêm data attribute vào HTML
4. Chạy script cập nhật

### **Thêm trang mới:**
1. Tạo trang HTML
2. Thêm data attributes
3. Include `js/config.js`
4. Tự động hoạt động

---

**Hệ thống cấu hình tập trung đã sẵn sàng! Chỉ cần sửa 1 file, toàn bộ website sẽ tự động cập nhật! ⚙️✨**
