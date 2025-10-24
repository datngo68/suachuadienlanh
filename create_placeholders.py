#!/usr/bin/env python3
"""
Script quản lý ảnh cho website điện lạnh
Chạy: python create_placeholders.py
"""

import os
import shutil
from datetime import datetime

def create_placeholder_images():
    """Tạo ảnh placeholder đơn giản"""
    
    # Tạo thư mục nếu chưa có
    os.makedirs('images/banner', exist_ok=True)
    os.makedirs('images/services', exist_ok=True)
    os.makedirs('images/placeholder', exist_ok=True)
    
    # Danh sách ảnh cần tạo
    images_to_create = [
        # Banner
        'images/banner/hero-bg.jpg',
        'images/banner/about-us.jpg',
        
        # Services
        'images/services/service-air-conditioner.jpg',
        'images/services/service-washing-machine.jpg',
        'images/services/service-refrigerator.jpg',
        'images/services/service-water-heater.jpg',
        'images/services/service-induction-cooker.jpg',
        'images/services/service-microwave.jpg',
        
        # Placeholder
        'images/placeholder/news-1.jpg',
        'images/placeholder/news-2.jpg',
        'images/placeholder/news-3.jpg',
        'images/placeholder/news-featured.jpg',
        'images/placeholder/team-1.jpg',
        'images/placeholder/team-2.jpg',
        'images/placeholder/team-3.jpg',
        'images/placeholder/about-company.jpg',
        'images/placeholder/article-air-conditioner.jpg',
        'images/placeholder/related-1.jpg',
        'images/placeholder/related-2.jpg',
        'images/placeholder/related-3.jpg',
        
        # Logo
        'images/logo.png'
    ]
    
    print("Tao anh placeholder...")
    
    # Tạo file placeholder đơn giản
    for image_path in images_to_create:
        if not os.path.exists(image_path):
            # Tạo file text thay thế (để tránh lỗi 404)
            with open(image_path, 'w', encoding='utf-8') as f:
                f.write(f"# Placeholder for {image_path}\n")
                f.write("# Thay the file nay bang anh that\n")
                f.write(f"# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            print(f"Tao placeholder: {image_path}")
    
    print("Hoan thanh tao placeholder!")

def check_image_status():
    """Kiểm tra trạng thái ảnh"""
    print("\n" + "="*50)
    print("KIEM TRA TRANG THAI ANH")
    print("="*50)
    
    # Danh sách ảnh cần kiểm tra
    all_images = [
        'images/banner/hero-bg.jpg',
        'images/banner/about-us.jpg',
        'images/services/service-air-conditioner.jpg',
        'images/services/service-washing-machine.jpg',
        'images/services/service-refrigerator.jpg',
        'images/services/service-water-heater.jpg',
        'images/services/service-induction-cooker.jpg',
        'images/services/service-microwave.jpg',
        'images/placeholder/news-1.jpg',
        'images/placeholder/news-2.jpg',
        'images/placeholder/news-3.jpg',
        'images/placeholder/news-featured.jpg',
        'images/placeholder/team-1.jpg',
        'images/placeholder/team-2.jpg',
        'images/placeholder/team-3.jpg',
        'images/placeholder/about-company.jpg',
        'images/placeholder/article-air-conditioner.jpg',
        'images/placeholder/related-1.jpg',
        'images/placeholder/related-2.jpg',
        'images/placeholder/related-3.jpg',
        'images/logo.png'
    ]
    
    placeholder_count = 0
    real_image_count = 0
    
    for image_path in all_images:
        if os.path.exists(image_path):
            file_size = os.path.getsize(image_path)
            if file_size < 1000:  # File nhỏ hơn 1KB = placeholder
                print(f"[PLACEHOLDER] {image_path} - Placeholder ({file_size} bytes)")
                placeholder_count += 1
            else:
                print(f"[REAL IMAGE] {image_path} - Anh that ({file_size:,} bytes)")
                real_image_count += 1
        else:
            print(f"[MISSING] {image_path} - Khong ton tai")
    
    print(f"\n[TONG KET]")
    print(f"   - Anh that: {real_image_count}")
    print(f"   - Placeholder: {placeholder_count}")
    print(f"   - Tong cong: {len(all_images)}")

def backup_images():
    """Sao lưu ảnh hiện tại"""
    backup_dir = f"images_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    if os.path.exists('images'):
        print(f"Sao luu anh vao: {backup_dir}")
        shutil.copytree('images', backup_dir)
        print(f"[SUCCESS] Da sao luu thanh cong!")
    else:
        print("[ERROR] Khong tim thay thu muc images")

def show_help():
    """Hiển thị hướng dẫn sử dụng"""
    print("\n" + "="*60)
    print("HUONG DAN SU DUNG SCRIPT")
    print("="*60)
    print("1. Tao placeholder: python create_placeholders.py")
    print("2. Kiem tra trang thai: python create_placeholders.py --check")
    print("3. Sao luu anh: python create_placeholders.py --backup")
    print("4. Tai anh tu website: python download_images_advanced.py")
    print("\nCAC LENH KHAC:")
    print("   --help: Hien thi huong dan nay")
    print("   --check: Kiem tra trang thai anh")
    print("   --backup: Sao luu anh hien tai")

def main():
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "--check":
            check_image_status()
        elif command == "--backup":
            backup_images()
        elif command == "--help":
            show_help()
        else:
            print(f"Lenh khong hop le: {command}")
            show_help()
    else:
        print("=" * 60)
        print("SCRIPT QUAN LY ANH WEBSITE DIEN LANH")
        print("=" * 60)
        
        create_placeholder_images()
        check_image_status()
        
        print("\n" + "="*50)
        print("HUONG DAN TIEP THEO:")
        print("="*50)
        print("1. Chay: python download_images_advanced.py")
        print("2. Hoac tai anh thu cong tu: https://suachuadienlanh247.vn/")
        print("3. Xem file: THAY_ANH_NHANH.md")
        print("\nCAC LENH HUU ICH:")
        print("   python create_placeholders.py --check")
        print("   python create_placeholders.py --backup")
        print("   python create_placeholders.py --help")

if __name__ == "__main__":
    main()
