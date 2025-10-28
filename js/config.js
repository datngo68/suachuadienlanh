/**
 * Cấu hình tập trung cho website điện lạnh
 * Chỉ cần sửa thông tin ở đây, toàn bộ website sẽ tự động cập nhật
 */

const WEBSITE_CONFIG = {
    // Thông tin công ty
    company: {
        name: "Sửa Chữa Điện Lạnh 247",
        fullName: "Dịch vụ sửa chữa điện lạnh 24/7",
        slogan: "Chi phí thấp - Đảm bảo kỹ thuật - Phục vụ tận tình"
    },

    // Thông tin liên hệ
    contact: {
        phone: "0936.255.627",
        phoneRaw: "0936255627", // Số điện thoại không dấu chấm
        zalo: "0936.255.627",
        zaloRaw: "0936255627", // Số Zalo không dấu chấm
        email: "suachuadienlanh247vn@gmail.com",
        website: "suachuadienlanh247.vn"
    },

    // Địa chỉ các cơ sở
    addresses: [
        {
            name: "Cơ sở chính 1",
            address: "52 Lê Thánh Tông, Ngô Quyền, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở chính 2",
            address: "16 Đông Khê, Ngô Quyền, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở 3",
            address: "122 Thiên Lôi, Lê Chân, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở 4",
            address: "325 Chợ Hàng, Lê Chân, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở 5",
            address: "Khu 3 Đẩu Sơn, Kiến An, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở 6",
            address: "Khu 3 Xã Hợp Đức, Đồ Sơn, Hải Phòng",
            phone: "0936.255.627"
        },
        {
            name: "Cơ sở 7",
            address: "87 Đằng Hải, Hải An, Hải Phòng",
            phone: "0936.255.627"
        }
    ],

    // Mạng xã hội
    social: {
        facebook: "#", // Thay bằng link Facebook thật
        youtube: "#",  // Thay bằng link YouTube thật
        zalo: "https://zalo.me/0936255627"
    },

    // Dịch vụ
    services: [
        {
            name: "Sửa Điều Hòa",
            slug: "sua-dieu-hoa",
            description: "Sửa chữa điều hòa không lạnh, không lên, làm lạnh chậm"
        },
        {
            name: "Sửa Máy Giặt",
            slug: "sua-may-giat",
            description: "Sửa chữa máy giặt không vắt, không xả nước, kêu to"
        },
        {
            name: "Sửa Tủ Lạnh",
            slug: "sua-tu-lanh",
            description: "Sửa chữa tủ lạnh không đông, không lên điện, kêu to"
        },
        {
            name: "Sửa Bình Nóng Lạnh",
            slug: "sua-binh-nong-lanh",
            description: "Sửa chữa bình nóng lạnh không có nước nóng, rò điện"
        },
        {
            name: "Sửa Bếp Từ",
            slug: "sua-bep-tu",
            description: "Sửa chữa bếp từ không nóng, không hoạt động"
        },
        {
            name: "Sửa Lò Vi Sóng",
            slug: "sua-lo-vi-song",
            description: "Sửa chữa lò vi sóng không nóng, không hoạt động"
        }
    ],

    // Khu vực phục vụ
    serviceAreas: [
        "Ngô Quyền", "Lê Chân", "Kiến An", "Đồ Sơn", "Hải An",
        "Dương Kinh", "An Dương", "An Lão", "Bạch Long Vĩ",
        "Cát Hải", "Kiến Thụy", "Thủy Nguyên", "Tiên Lãng", "Vĩnh Bảo"
    ],

    // Thông tin SEO
    seo: {
        title: "Sửa Chữa Điện Lạnh 247 - Dịch vụ sửa chữa tại nhà Hải Phòng",
        description: "Dịch vụ sửa chữa điện lạnh 24/7 tại Hải Phòng. Sửa điều hòa, máy giặt, tủ lạnh, bình nóng lạnh, bếp từ, lò vi sóng. Hotline: 033.6288.248",
        keywords: "sửa điện lạnh, sửa điều hòa, sửa máy giặt, sửa tủ lạnh, hải phòng, 24/7"
    }
};

/**
 * Hàm cập nhật thông tin liên hệ trên trang
 */
function updateContactInfo() {
    // Cập nhật số điện thoại
    const phoneElements = document.querySelectorAll('[data-phone]');
    phoneElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.contact.phone;
        el.href = `tel:${WEBSITE_CONFIG.contact.phoneRaw}`;
    });

    // Cập nhật số Zalo
    const zaloElements = document.querySelectorAll('[data-zalo]');
    zaloElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.contact.zalo;
        el.href = `https://zalo.me/${WEBSITE_CONFIG.contact.zaloRaw}`;
    });

    // Cập nhật email
    const emailElements = document.querySelectorAll('[data-email]');
    emailElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.contact.email;
        el.href = `mailto:${WEBSITE_CONFIG.contact.email}`;
    });

    // Cập nhật website
    const websiteElements = document.querySelectorAll('[data-website]');
    websiteElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.contact.website;
        el.href = `https://${WEBSITE_CONFIG.contact.website}`;
    });

    // Cập nhật tên công ty
    const companyElements = document.querySelectorAll('[data-company-name]');
    companyElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.company.name;
    });

    // Cập nhật slogan
    const sloganElements = document.querySelectorAll('[data-slogan]');
    sloganElements.forEach(el => {
        el.textContent = WEBSITE_CONFIG.company.slogan;
    });
}

/**
 * Hàm cập nhật địa chỉ các cơ sở
 */
function updateAddresses() {
    const addressContainer = document.getElementById('addresses-list');
    if (addressContainer) {
        let html = '';
        WEBSITE_CONFIG.addresses.forEach(addr => {
            html += `
                <div class="location-item">
                    <h4>${addr.name}</h4>
                    <p><i class="fas fa-map-marker-alt"></i> ${addr.address}</p>
                    <p><i class="fas fa-phone"></i> ${addr.phone}</p>
                </div>
            `;
        });
        addressContainer.innerHTML = html;
    }
}

/**
 * Hàm cập nhật khu vực phục vụ
 */
function updateServiceAreas() {
    const areasContainer = document.getElementById('service-areas-list');
    if (areasContainer) {
        let html = '';
        WEBSITE_CONFIG.serviceAreas.forEach(area => {
            html += `<span class="service-area-tag">${area}</span>`;
        });
        areasContainer.innerHTML = html;
    }
}

/**
 * Hàm cập nhật social links
 */
function updateSocialLinks() {
    // Facebook
    const facebookLinks = document.querySelectorAll('[data-facebook]');
    facebookLinks.forEach(el => {
        el.href = WEBSITE_CONFIG.social.facebook;
    });

    // YouTube
    const youtubeLinks = document.querySelectorAll('[data-youtube]');
    youtubeLinks.forEach(el => {
        el.href = WEBSITE_CONFIG.social.youtube;
    });

    // Zalo
    const zaloLinks = document.querySelectorAll('[data-zalo-link]');
    zaloLinks.forEach(el => {
        el.href = WEBSITE_CONFIG.social.zalo;
    });
}

/**
 * Hàm khởi tạo - chạy khi trang load
 */
function initConfig() {
    updateContactInfo();
    updateAddresses();
    updateServiceAreas();
    updateSocialLinks();

    console.log('✅ Website config đã được khởi tạo');
}

// Chạy khi DOM đã load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initConfig);
} else {
    initConfig();
}
