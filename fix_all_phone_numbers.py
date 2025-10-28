#!/usr/bin/env python3
"""
Script để sửa tất cả số điện thoại và thêm data attributes
"""

import os
import re

def fix_phone_numbers(file_path):
    """Sửa số điện thoại và thêm data attributes"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Sửa số điện thoại cũ thành mới
        content = content.replace('033.6288.248', '0936.255.627')
        content = content.replace('0336288248', '0936255627')
        
        # Thêm data attributes cho các link tel: chưa có
        content = re.sub(
            r'<a href="tel:0936255627"([^>]*)>([^<]*)</a>',
            lambda m: f'<a href="tel:0936255627"{m.group(1)} data-phone>{m.group(2)}</a>' if 'data-phone' not in m.group(1) else m.group(0),
            content
        )
        
        # Thêm data attributes cho các link zalo chưa có
        content = re.sub(
            r'<a href="https://zalo\.me/0936255627"([^>]*)>([^<]*)</a>',
            lambda m: f'<a href="https://zalo.me/0936255627"{m.group(1)} data-zalo-link>{m.group(2)}</a>' if 'data-zalo-link' not in m.group(1) else m.group(0),
            content
        )
        
        # Thêm data attributes cho số điện thoại trong text
        content = re.sub(
            r'<strong>033\.6288\.888</strong>',
            '<strong data-phone>0936.255.627</strong>',
            content
        )
        
        content = re.sub(
            r'<p><i class="fas fa-phone"></i> 033\.6288\.888</p>',
            '<p><i class="fas fa-phone"></i> <span data-phone>0936.255.627</span></p>',
            content
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
    print("Bat dau sua tat ca so dien thoai va them data attributes...")
    
    html_files = [
        'gioi-thieu.html',
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
            if fix_phone_numbers(file_path):
                updated_count += 1
        else:
            print(f"[WARNING] File khong ton tai: {file_path}")
    
    print(f"\n[SUCCESS] Hoan thanh! Da cap nhat {updated_count} file")
    print("\nCac thay doi da thuc hien:")
    print("1. Sua tat ca so dien thoai tu 033.6288.248 thanh 0936.255.627")
    print("2. Them data-phone cho tat ca link tel:")
    print("3. Them data-zalo-link cho tat ca link zalo")
    print("4. Them data attributes cho so dien thoai trong text")

if __name__ == "__main__":
    main()
