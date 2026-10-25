[app]

# (str) Title of your application
title = Auto Macro App

# (str) Package name
package.name = automacroapp

# (str) Package domain (needed for android packaging)
package.domain = org.huyxaa06

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,opencv,numpy

# (str) Application versioning
version = 0.1

# (str) Supported orientations
orientation = portrait

# List of permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Accept Android SDK licenses automatically
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
