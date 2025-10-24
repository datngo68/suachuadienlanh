#!/usr/bin/env python3
"""
Script nâng cao để tải ảnh từ website suachuadienlanh247.vn
Chạy: python download_images_advanced.py
"""

import requests
import os
import time
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

def download_image(url, filename, headers=None):
    """Tải ảnh từ URL và lưu vào file"""
    try:
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        
        print(f"Đang tải: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Kiểm tra content-type
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print(f"⚠️  Không phải ảnh: {url}")
            return False
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        file_size = len(response.content)
        print(f"✅ Đã tải: {filename} ({file_size:,} bytes)")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi tải {url}: {e}")
        return False

def find_images_on_page(url):
    """Tìm tất cả ảnh trên trang web"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        print(f"Đang phân tích trang: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        images = []
        
        # Tìm tất cả thẻ img
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                # Chuyển relative URL thành absolute URL
                full_url = urljoin(url, src)
                alt = img.get('alt', '')
                images.append({
                    'url': full_url,
                    'alt': alt,
                    'src': src
                })
        
        return images
        
    except Exception as e:
        print(f"❌ Lỗi phân tích trang {url}: {e}")
        return []

def create_image_mapping():
    """Tạo mapping giữa ảnh cần tải và URL có thể có"""
    return {
        # Banner images
        'images/banner/hero-bg.jpg': [
            'https://suachuadienlanh247.vn/',
            'hero', 'banner', 'main', 'background'
        ],
        'images/banner/about-us.jpg': [
            'https://suachuadienlanh247.vn/',
            'about', 'gioi-thieu', 'company'
        ],
        
        # Service images
        'images/services/service-air-conditioner.jpg': [
            'https://suachuadienlanh247.vn/',
            'dieu-hoa', 'air-conditioner', 'may-lanh'
        ],
        'images/services/service-washing-machine.jpg': [
            'https://suachuadienlanh247.vn/',
            'may-giat', 'washing-machine', 'giặt'
        ],
        'images/services/service-refrigerator.jpg': [
            'https://suachuadienlanh247.vn/',
            'tu-lanh', 'refrigerator', 'tủ lạnh'
        ],
        'images/services/service-water-heater.jpg': [
            'https://suachuadienlanh247.vn/',
            'binh-nong-lanh', 'water-heater', 'bình nóng lạnh'
        ],
        'images/services/service-induction-cooker.jpg': [
            'https://suachuadienlanh247.vn/',
            'bep-tu', 'induction', 'bếp từ'
        ],
        'images/services/service-microwave.jpg': [
            'https://suachuadienlanh247.vn/',
            'lo-vi-song', 'microwave', 'lò vi sóng'
        ],
        
        # News images
        'images/placeholder/news-1.jpg': [
            'https://suachuadienlanh247.vn/',
            'tin-tuc', 'news', 'bai-viet'
        ],
        'images/placeholder/news-2.jpg': [
            'https://suachuadienlanh247.vn/',
            'tin-tuc', 'news', 'bai-viet'
        ],
        'images/placeholder/news-3.jpg': [
            'https://suachuadienlanh247.vn/',
            'tin-tuc', 'news', 'bai-viet'
        ],
        'images/placeholder/news-featured.jpg': [
            'https://suachuadienlanh247.vn/',
            'tin-tuc', 'news', 'featured', 'nổi bật'
        ],
        
        # Team images
        'images/placeholder/team-1.jpg': [
            'https://suachuadienlanh247.vn/',
            'doi-ngu', 'team', 'ky-thuat-vien'
        ],
        'images/placeholder/team-2.jpg': [
            'https://suachuadienlanh247.vn/',
            'doi-ngu', 'team', 'ky-thuat-vien'
        ],
        'images/placeholder/team-3.jpg': [
            'https://suachuadienlanh247.vn/',
            'doi-ngu', 'team', 'ky-thuat-vien'
        ],
        
        # Other images
        'images/placeholder/about-company.jpg': [
            'https://suachuadienlanh247.vn/',
            'about', 'company', 'cong-ty'
        ],
        'images/logo.png': [
            'https://suachuadienlanh247.vn/',
            'logo', 'brand'
        ]
    }

def smart_download_images():
    """Tải ảnh thông minh từ website"""
    print("🚀 Bắt đầu tải ảnh từ website...")
    
    # Tạo thư mục
    os.makedirs('images/banner', exist_ok=True)
    os.makedirs('images/services', exist_ok=True)
    os.makedirs('images/placeholder', exist_ok=True)
    
    # Lấy danh sách ảnh từ trang chủ
    main_url = 'https://suachuadienlanh247.vn/'
    images = find_images_on_page(main_url)
    
    if not images:
        print("❌ Không tìm thấy ảnh nào trên trang chủ")
        return
    
    print(f"📸 Tìm thấy {len(images)} ảnh trên trang chủ")
    
    # Mapping ảnh cần tải
    image_mapping = create_image_mapping()
    
    downloaded_count = 0
    
    for target_file, keywords in image_mapping.items():
        if os.path.exists(target_file):
            print(f"⏭️  Bỏ qua (đã tồn tại): {target_file}")
            continue
            
        print(f"\n🔍 Tìm ảnh cho: {target_file}")
        
        best_match = None
        best_score = 0
        
        for img in images:
            score = 0
            img_url = img['url'].lower()
            img_alt = img['alt'].lower()
            
            # Tính điểm dựa trên keywords
            for keyword in keywords:
                if keyword.lower() in img_url or keyword.lower() in img_alt:
                    score += 1
            
            if score > best_score:
                best_score = score
                best_match = img
        
        if best_match and best_score > 0:
            print(f"🎯 Tìm thấy ảnh phù hợp (điểm: {best_score})")
            if download_image(best_match['url'], target_file):
                downloaded_count += 1
                time.sleep(1)  # Nghỉ 1 giây giữa các lần tải
        else:
            print(f"❌ Không tìm thấy ảnh phù hợp cho {target_file}")
    
    print(f"\n✅ Hoàn thành! Đã tải {downloaded_count} ảnh")
    
    if downloaded_count == 0:
        print("\n💡 Gợi ý:")
        print("1. Kiểm tra kết nối internet")
        print("2. Thử tải ảnh thủ công từ website")
        print("3. Sử dụng file THAY_ANH_NHANH.md để hướng dẫn")

def main():
    print("=" * 60)
    print("🖼️  SCRIPT TẢI ẢNH TỪ WEBSITE ĐIỆN LẠNH 247")
    print("=" * 60)
    
    try:
        smart_download_images()
    except KeyboardInterrupt:
        print("\n⏹️  Đã dừng bởi người dùng")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        print("\n💡 Thử tải ảnh thủ công theo hướng dẫn trong THAY_ANH_NHANH.md")

if __name__ == "__main__":
    main()
