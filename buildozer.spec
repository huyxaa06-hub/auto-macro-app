[app]

# (str) Title of your application
title = Auto Macro App

# (str) Package name
package.name = automacroapp

# (str) Package domain (needed for android packaging)
package.domain = org.huyxaa06

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Thêm các thư viện Python mà ứng dụng của bạn đang dùng vào đây (ví dụ: python3, tkinter, opencv, numpy...)
requirements = python3,kivy,opencv,numpy

# (str) Supported orientations
orientation = portrait

# List of permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
