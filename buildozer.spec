[app]
# Uygulama Bilgileri
title = Jarvis Ultra
package.name = jarvis_ultra
package.domain = org.huseyin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 1.0

# Gerekli Kütüphaneler
# pyjnius: Android donanımına (ses, titreşim) erişim sağlar
# requests: İnternet işlemleri için
requirements = python3,kivy,pyjnius,requests

orientation = portrait

# ANDROID İZİNLERİ (Sizin için hepsini ekledim)
# INTERNET: Güncellemeler için
# VIBRATE: Fiziksel tepki için
# READ/WRITE_EXTERNAL_STORAGE: Kodları telefonda saklayıp düzenlemeniz için
android.permissions = INTERNET, VIBRATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, FLASHLIGHT

# Ekranın kapanmasını engelle (Asistan modunda açık kalsın)
android.wakelock = True

# Android Mimarileri (Yeni telefonların çoğu için uygundur)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
