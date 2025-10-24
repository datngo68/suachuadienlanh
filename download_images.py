#!/usr/bin/env python3
"""
Script để tải ảnh từ website suachuadienlanh247.vn
Chạy: python download_images.py
"""

import requests
import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

def download_image(url, filename):
    """Tải ảnh từ URL và lưu vào file"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"✅ Đã tải: {filename}")
        return True
    except Exception as e:
        print(f"❌ Lỗi tải {url}: {e}")
        return False

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
    
    print("🖼️  Tạo ảnh placeholder...")
    
    # Tạo file placeholder đơn giản
    for image_path in images_to_create:
        if not os.path.exists(image_path):
            # Tạo file text thay thế (để tránh lỗi 404)
            with open(image_path, 'w') as f:
                f.write(f"# Placeholder for {image_path}\n")
                f.write("# Thay thế file này bằng ảnh thật\n")
            print(f"📝 Tạo placeholder: {image_path}")
    
    print("✅ Hoàn thành tạo placeholder!")

def main():
    print("🚀 Bắt đầu tạo ảnh placeholder...")
    create_placeholder_images()
    
    print("\n📋 Hướng dẫn tiếp theo:")
    print("1. Truy cập https://suachuadienlanh247.vn/")
    print("2. Tải ảnh cần thiết từ website")
    print("3. Thay thế các file placeholder bằng ảnh thật")
    print("4. Đảm bảo tên file giống với placeholder")
    
    print("\n💡 Mẹo:")
    print("- Sử dụng Ctrl+S để lưu ảnh từ website")
    print("- Đặt tên file giống với placeholder")
    print("- Nén ảnh để tăng tốc độ tải")

if __name__ == "__main__":
    main()
