from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        # Arka planı tamamen siyah yapıyoruz ki hologram parlasın
        Window.clearcolor = (0, 0, 0, 1)
        
        self.layout = FloatLayout()

        # 1. DÖNEN HOLOGRAM RESMİ
        # Dosya adını 'jarvis.png' olarak ayarladım çünkü GitHub'a öyle yüklediniz
        self.hologram = Image(
            source='jarvis.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, 0.9)
        )
        self.layout.add_widget(self.hologram)

        # 2. ALT YAZI
        self.status_label = Label(
            text="[b]JARVIS SISTEMI AKTIF[/b]",
            markup=True,
            font_size='22sp',
            color=(0, 0.8, 1, 1), # Neon Mavi
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )
        self.layout.add_widget(self.status_label)

        # Resmi saniyede 60 kez döndürerek hareket sağlıyoruz
        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        
        return self.layout

    def dondur(self, dt):
        # Her karede 1 derece döner
        self.hologram.rotation += 1

if __name__ == "__main__":
    JarvisApp().run()
