from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()
        
        # Hafıza (İsimsiz ve sade)
        self.hafiza = {"selam": "Merhaba, sistem aktif."}

        # 1. HOLOGRAM (Dönüş hızı ayarlandı)
        self.hologram = Image(
            source='jarvis.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.55}, 
            size_hint=(0.7, 0.7)
        )
        self.layout.add_widget(self.hologram)

        # 2. DURUM MESAJI
        self.status = Label(
            text="Sistem Yükleniyor...", 
            pos_hint={'center_x': 0.5, 'center_y': 0.2}, 
            color=(0, 1, 1, 1)
        )
        self.layout.add_widget(self.status)

        # 3. KOMUT GİRİŞİ
        self.input_box = TextInput(
            hint_text='Komut bekleniyor...', 
            size_hint=(0.8, 0.06), 
            pos_hint={'center_x': 0.5, 'center_y': 0.1}, 
            multiline=False
        )
        self.input_box.bind(on_text_validate=self.cevap_ver)
        self.layout.add_widget(self.input_box)

        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        Clock.schedule_once(self.sistemi_baslat, 2)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def sistemi_baslat(self, dt):
        self.status.text = "Jarvis Ultra Hazır."

    def cevap_ver(self, instance):
        soru = self.input_box.text.lower()
        self.input_box.text = ""
        self.status.text = self.hafiza.get(soru, "Bu komut sistemde tanımlı değil.")

if __name__ == "__main__":
    JarvisApp().run()
