[app]
title = Jarvis Huseyin
package.name = jarvis_huseyin
package.domain = org.huseyin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 0.1

# BURASI ÇOK ÖNEMLİ: pyjnius ekledik!
requirements = python3,kivy,pyjnius

orientation = portrait

# YETKİLER: Titreşim ve Fener için
android.permissions = VIBRATE, CAMERA, FLASHLIGHT

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
