import urllib.request
import os
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from jnius import autoclass

class JarvisApp(App):
    def build(self):
        # Arka plan simsiyah
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()

        # 1. GÜNCELLEME SİSTEMİ
        Clock.schedule_once(self.sistemi_denetle, 2)

        # 2. DÖNEN HOLOGRAM (jarvis.png dosyanız)
        self.hologram = Image(
            source='jarvis.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.85, 0.85)
        )
        self.layout.add_widget(self.hologram)

        # 3. TEKNİK VERİLER (Karizma için sol üstte)
        self.data_label = Label(
            text="CORE: RUNNING\nUPLINK: SECURED\nAUTO_OTA: ACTIVE",
            font_size='12sp',
            color=(0, 1, 1, 0.5),
            halign='left',
            pos_hint={'center_x': 0.2, 'center_y': 0.9}
        )
        self.layout.add_widget(self.data_label)

        # 4. SİSTEM DURUM MESAJI (Alt orta)
        self.status = Label(
            text="Sistem hazır.",
            font_size='18sp',
            color=(1, 1, 1, 0.7),
            pos_hint={'center_x': 0.5, 'center_y': 0.15}
        )
        self.layout.add_widget(self.status)

        # 5. GİZLİ DOKUNMATİK PANEL (Holograma dokununca çalışır)
        self.btn = Button(
            background_color=(0,0,0,0), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.6, 0.6)
        )
        self.btn.bind(on_press=self.aksiyon)
        self.layout.add_widget(self.btn)

        # Görseli döndürmeye başla
        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def sistemi_denetle(self, dt):
        self.status.text = "Protokoller güncelleniyor..."
        # Burada ileride logic.py dosyasını GitHub'dan çekeceğiz
        Clock.schedule_once(lambda x: setattr(self.status, 'text', "Sistem %100 güncel."), 3)

    def aksiyon(self, instance):
        try:
            # Android fiziksel tepki (Titreşim)
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(150) # Kısa bir 'onay' titreşimi
            
            mesajlar = ["ANALİZ TAMAMLANDI", "VERİ TABANI AKTİF", "TARAMA BAŞARILI"]
            self.status.text = random.choice(mesajlar)
        except:
            self.status.text = "SİSTEM ÇEVRİMDIŞI MODDA"

if __name__ == "__main__":
    JarvisApp().run()
