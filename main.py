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
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()

        # 1. GÜNCELLEME KONTROLÜ (Arka Planda Çalışır)
        Clock.schedule_once(self.sistemi_guncelle, 1)

        # 2. MERKEZİ DÖNEN HOLOGRAM (jarvis.png)
        self.hologram = Image(
            source='jarvis.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.85, 0.85)
        )
        self.layout.add_widget(self.hologram)

        # 3. TEKNİK VERİLER (İsimsiz, Sadece Sistem Bilgisi)
        self.data_label = Label(
            text="CORE_STATUS: RUNNING\nUPLINK: SECURED\nAUTO_UPDATE: ENABLED",
            font_size='12sp',
            color=(0, 1, 1, 0.6),
            pos_hint={'center_x': 0.2, 'center_y': 0.9}
        )
        self.layout.add_widget(self.data_label)

        # 4. DURUM MESAJI
        self.status = Label(
            text="Sistem hazır.",
            font_size='18sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.15}
        )
        self.layout.add_widget(self.status)

        # 5. GİZLİ DOKUNMATİK TETİKLEYİCİ
        self.btn = Button(background_color=(0,0,0,0), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.btn.bind(on_press=self.aksiyon)
        self.layout.add_widget(self.btn)

        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def sistemi_guncelle(self, dt):
        # NOT: Buradaki URL kısmına ileride logic.py linkini koyacağız
        self.status.text = "Güncellemeler denetleniyor..."
        # Şimdilik simüle ediyoruz, sistem hazır olduğunda gerçek indirme yapacak
        Clock.schedule_once(lambda x: setattr(self.status, 'text', "Sistem güncel."), 3)

    def aksiyon(self, instance):
        try:
            # Android Titreşim
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(100)
            
            mesajlar = ["ANALİZ TAMAMLANDI", "VERİ TABANI GÜNCEL", "GÜVENLİ BAĞLANTI"]
            self.status.text = random.choice(mesajlar)
        except:
            self.status.text = "ERİŞİM REDDEDİLDİ"

if __name__ == "__main__":
    JarvisApp().run()
