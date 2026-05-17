from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class JarvisApp(App):
    def build(self):
        # Arka planı koyu bir mavi yapalım
        Window.clearcolor = (0, 0.05, 0.1, 1)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Başlık
        self.label = Label(
            text="JARVIS SISTEMI AKTIF",
            font_size='30sp',
            color=(0, 0.8, 1, 1) # Neon Mavi
        )
        
        # Etkileşimli bir buton
        btn = Button(
            text="KOMUT VER",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0.8, 1)
        )
        btn.bind(on_press=self.komut_al)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def komut_al(self, instance):
        self.label.text = "Sizi dinliyorum Hüseyin Bey..."

if __name__ == "__main__":
    JarvisApp().run()
