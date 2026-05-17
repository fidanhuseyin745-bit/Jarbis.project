[app]
title = Jarvis Ultra Core
package.name = jarvis_ultracore
package.domain = org.huseyin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
version = 1.0

# GEREKLİ KÜTÜPHANELER: pyjnius (donanım), requests (güncelleme)
requirements = python3,kivy,pyjnius,requests

orientation = portrait

# ANDROID İZİNLERİ: Ses kaydı, internet ve titreşim
android.permissions = INTERNET, VIBRATE, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, CAMERA, FLASHLIGHT

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
