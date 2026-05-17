[app]
title = Jarvis Core
package.name = jarvis_core
package.domain = org.huseyin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 1.0

# Gerekli kütüphaneler (Güncelleme ve Android erişimi için)
requirements = python3,kivy,pyjnius,requests

orientation = portrait

# ANDROID İZİNLERİ (Burayı ekledik)
android.permissions = INTERNET, VIBRATE, CAMERA, FLASHLIGHT

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
