import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()
        
        # Hafızayı sadece uygulama içine hapsedelim (Dış dosyaya erişip çökmesin)
        self.hafiza = {"selam": "Merhaba Hüseyin bey."}

        # 1. HOLOGRAM
        self.hologram = Image(source='jarvis.png', pos_hint={'center_x': 0.5, 'center_y': 0.55}, size_hint=(0.7, 0.7))
        self.layout.add_widget(self.hologram)

        # 2. DURUM
        self.status = Label(text="Güvenli Mod Aktif", pos_hint={'center_x': 0.5, 'center_y': 0.2}, color=(0, 1, 1, 1))
        self.layout.add_widget(self.status)

        # 3. GİRİŞ
        self.input_box = TextInput(hint_text='Komut...', size_hint=(0.8, 0.06), pos_hint={'center_x': 0.5, 'center_y': 0.1}, multiline=False)
        self.input_box.bind(on_text_validate=self.cevap_ver)
        self.layout.add_widget(self.input_box)

        # 4. GİZLİ ADM BUTONU (Panel açma)
        self.admin_btn = Button(text="ADM", size_hint=(0.1, 0.05), pos_hint={'right': 1, 'top': 1}, background_color=(0,0,0,0))
        self.admin_btn.bind(on_press=self.paneli_ac)
        self.layout.add_widget(self.admin_btn)

        # Çökme riskine karşı ses motorunu şimdilik devre dışı bıraktım
        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def paneli_ac(self, instance):
        self.status.text = "Panel yakında aktif edilecek."

    def cevap_ver(self, instance):
        soru = self.input_box.text.lower()
        self.input_box.text = ""
        self.status.text = self.hafiza.get(soru, "Anlaşılamadı.")

if __name__ == "__main__":
    JarvisApp().run()
