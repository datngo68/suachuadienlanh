#!/usr/bin/env python3
"""
Script để cập nhật tất cả icon Zalo trong website
"""

import os
import re

def update_zalo_icons_in_file(file_path):
    """Cập nhật icon Zalo trong một file HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Thêm floating button nếu chưa có
        if 'zalo-floating' not in content and '<!-- Footer -->' in content:
            content = content.replace(
                '    <!-- Footer -->',
                '''    <!-- Zalo Floating Button -->
    <a href="https://zalo.me/0336288248" class="zalo-floating" target="_blank" title="Chat Zalo">
    </a>

    <!-- Footer -->'''
            )
        
        # Thay thế icon Zalo cũ bằng icon mới
        # Pattern 1: <i class="fab fa-zalo"></i> trong button
        content = re.sub(
            r'<a href="https://zalo\.me/0336288248" class="btn btn-secondary" target="_blank">\s*<i class="fab fa-zalo"></i>',
            '<a href="https://zalo.me/0336288248" class="btn btn-secondary btn-zalo" target="_blank">\n                        <span class="zalo-icon"></span>',
            content
        )
        
        # Pattern 2: <i class="fab fa-zalo"></i> trong social link
        content = re.sub(
            r'<a href="#" class="social-link"><i class="fab fa-zalo"></i> Zalo</a>',
            '''<a href="https://zalo.me/0336288248" class="social-link" target="_blank">
                            <span class="zalo-icon"></span> Zalo
                        </a>''',
            content
        )
        
        # Pattern 3: <i class="fab fa-zalo"></i> trong contact icon
        content = re.sub(
            r'<div class="contact-icon">\s*<i class="fab fa-zalo"></i>\s*</div>',
            '<div class="contact-icon">\n                        <span class="zalo-icon"></span>\n                    </div>',
            content
        )
        
        # Pattern 4: <i class="fab fa-zalo"></i> trong button khác
        content = re.sub(
            r'<i class="fab fa-zalo"></i>',
            '<span class="zalo-icon"></span>',
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
    print("Bat dau cap nhat icon Zalo...")
    
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
            if update_zalo_icons_in_file(file_path):
                updated_count += 1
        else:
            print(f"[WARNING] File khong ton tai: {file_path}")
    
    print(f"\n[SUCCESS] Hoan thanh! Da cap nhat {updated_count} file")
    print("\nCac thay doi da thuc hien:")
    print("1. Them floating Zalo button vao tat ca trang")
    print("2. Thay the icon Zalo cu bang icon moi voi hieu ung")
    print("3. Cap nhat class CSS cho button Zalo")
    print("4. Them link Zalo vao social links")

if __name__ == "__main__":
    main()
