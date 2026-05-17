[app]
title = Jarvis Ultra
package.name = jarvis_ultra
package.domain = org.huseyin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 1.1

# Sadece temel kütüphaneler (Hata riskini azaltmak için)
requirements = python3,kivy

orientation = portrait
android.permissions = INTERNET, VIBRATE

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
