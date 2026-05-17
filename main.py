from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        # Arka plan rengini tamamen siyah yapıyoruz
        Window.clearcolor = (0, 0, 0, 1)
        
        self.layout = FloatLayout()

        # 1. HOLOGRAM RESMİ (Dönen kısım)
        # Buradaki 'hologram.png' isminin GitHub'a yüklediğiniz resimle AYNI olduğundan emin olun!
        self.hologram = Image(
            source='hologram.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.8)
        )
        self.layout.add_widget(self.hologram)

        # 2. YAZI KATMANI
        self.status_label = Label(
            text="[b]JARVIS CORE AKTİF[/b]",
            markup=True,
            font_size='24sp',
            color=(0, 0.8, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.15}
        )
        self.layout.add_widget(self.status_label)

        # HAREKETİ BAŞLAT: Her saniye 60 kez resmi döndür
        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        
        return self.layout

    def dondur(self, dt):
        # Resmi her karede 1 derece döndürür
        self.hologram.rotation += 1

if __name__ == "__main__":
    JarvisApp().run()

