[app]

# Tên ứng dụng của bạn
title = AutoGameLoader
package.name = autogameloader
package.domain = org.autogen

# Các file nguồn cần đưa vào APK (chứa app vỏ bọc loader_app.py)
source.include_exts = py,png,jpg,kv,atlas

# Danh sách thư viện ĐÓNG GÓI SẴN vào bên trong APK (Bắt buộc phải có các dòng này)
requirements = python3,kivy,requests,opencv-python,numpy

# Phiên bản hướng tới của Android
android.api = 33
android.minapi = 21

# Cấp quyền truy cập Internet để app có thể tải code từ GitHub về
android.permissions = INTERNET

# Hướng màn hình (portrait: dọc, landscape: ngang)
orientation = portrait
