#!/usr/bin/env python3
"""
Script để cập nhật tất cả trang HTML với data attributes cho cấu hình tập trung
"""

import os
import re

def update_html_file(file_path):
    """Cập nhật file HTML với data attributes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Thêm script config.js nếu chưa có
        if 'js/config.js' not in content and 'js/main.js' in content:
            content = content.replace(
                '<script src="js/main.js"></script>',
                '<script src="js/config.js"></script>\n    <script src="js/main.js"></script>'
            )
        
        # Cập nhật số điện thoại
        content = re.sub(
            r'<a href="tel:0336288248"[^>]*>033\.6288\.248</a>',
            '<a href="tel:0336288248" data-phone>033.6288.248</a>',
            content
        )
        
        # Cập nhật email
        content = re.sub(
            r'<a href="mailto:suachuadienlanh247vn@gmail\.com"[^>]*>suachuadienlanh247vn@gmail\.com</a>',
            '<a href="mailto:suachuadienlanh247vn@gmail.com" data-email>suachuadienlanh247vn@gmail.com</a>',
            content
        )
        
        # Cập nhật website
        content = re.sub(
            r'<a href="https://suachuadienlanh247\.vn"[^>]*>suachuadienlanh247\.vn</a>',
            '<a href="https://suachuadienlanh247.vn" data-website>suachuadienlanh247.vn</a>',
            content
        )
        
        # Cập nhật Facebook link
        content = re.sub(
            r'<a href="#" class="social-link"><i class="fab fa-facebook"></i> Facebook</a>',
            '<a href="#" class="social-link" data-facebook><i class="fab fa-facebook"></i> Facebook</a>',
            content
        )
        
        # Cập nhật YouTube link
        content = re.sub(
            r'<a href="#" class="social-link"><i class="fab fa-youtube"></i> YouTube</a>',
            '<a href="#" class="social-link" data-youtube><i class="fab fa-youtube"></i> YouTube</a>',
            content
        )
        
        # Cập nhật Zalo link
        content = re.sub(
            r'<a href="https://zalo\.me/0336288248" class="social-link"[^>]*>',
            '<a href="https://zalo.me/0336288248" class="social-link" target="_blank" data-zalo-link>',
            content
        )
        
        # Cập nhật floating Zalo button
        content = re.sub(
            r'<a href="https://zalo\.me/0336288248" class="zalo-floating"[^>]*>',
            '<a href="https://zalo.me/0336288248" class="zalo-floating" target="_blank" title="Chat Zalo" data-zalo-link>',
            content
        )
        
        # Thêm container cho địa chỉ nếu chưa có
        if 'id="addresses-list"' not in content and 'location-item' in content:
            # Tìm và thay thế section địa chỉ
            content = re.sub(
                r'(<div class="locations-grid">)(.*?)(</div>)',
                r'\1<div id="addresses-list">\2</div>\3',
                content,
                flags=re.DOTALL
            )
        
        # Thêm container cho khu vực phục vụ nếu chưa có
        if 'id="service-areas-list"' not in content and 'service-area' in content:
            content = re.sub(
                r'(<div class="service-areas">)(.*?)(</div>)',
                r'\1<div id="service-areas-list">\2</div>\3',
                content,
                flags=re.DOTALL
            )
        
        # Chỉ ghi file nếu có thay đổi
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[SUCCESS] Da cap nhat: {file_path}")
            return True
        else:
            print(f"[SKIP] Khong can cap nhat: {file_path}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Loi cap nhat {file_path}: {e}")
        return False

def main():
    print("Bat dau cap nhat data attributes cho cau hinh tap trung...")
    
    # Danh sách file HTML cần cập nhật
    html_files = [
        'index.html',
        'gioi-thieu.html',
        'lien-he.html',
        'dich-vu/sua-dieu-hoa.html',
        'dich-vu/sua-may-giat.html',
        'dich-vu/sua-tu-lanh.html',
        'dich-vu/sua-binh-nong-lanh.html',
        'dich-vu/sua-bep-tu.html',
        'dich-vu/sua-lo-vi-song.html',
        'tin-tuc/index.html',
        'tin-tuc/bai-viet/huong-dan-tu-sua-dieu-hoa.html'
    ]
    
    updated_count = 0
    
    for file_path in html_files:
        if os.path.exists(file_path):
            if update_html_file(file_path):
                updated_count += 1
        else:
            print(f"[WARNING] File khong ton tai: {file_path}")
    
    print(f"\n[SUCCESS] Hoan thanh! Da cap nhat {updated_count} file")
    print("\nCac thay doi da thuc hien:")
    print("1. Them script config.js vao tat ca trang")
    print("2. Them data attributes cho thong tin lien he")
    print("3. Them data attributes cho social links")
    print("4. Them container cho dia chi va khu vuc phuc vu")
    print("\nBay gio ban co the sua thong tin trong file js/config.js")

if __name__ == "__main__":
    main()
