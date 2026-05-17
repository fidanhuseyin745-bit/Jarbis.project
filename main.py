from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
from jnius import autoclass
import random

class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()

        # 1. HOLOGRAM
        self.hologram = Image(source='jarvis.png', pos_hint={'center_x': 0.5, 'center_y': 0.53}, size_hint=(0.7, 0.7))
        self.layout.add_widget(self.hologram)

        # 2. GİRİŞ ALANI
        self.input_box = TextInput(
            hint_text='Mesajınızı yazın...', size_hint=(0.8, 0.06),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_color=(0, 0, 0, 0.6), foreground_color=(0, 1, 1, 1), multiline=False
        )
        self.input_box.bind(on_text_validate=self.jarvis_islem)
        self.layout.add_widget(self.input_box)

        # 3. DURUM ETİKETİ
        self.status = Label(text="Sistem Öğrenmeye Hazır.", pos_hint={'center_x': 0.5, 'center_y': 0.18}, color=(0, 1, 1, 0.8))
        self.layout.add_widget(self.status)

        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def sesli_konus(self, mesaj):
        # Android'in kendi ses motorunu (TTS) kullanır
        try:
            Locale = autoclass('java.util.Locale')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            # Ses motorunu başlat
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.tts.setLanguage(Locale.getDefault())
            self.tts.speak(mesaj, TextToSpeech.QUEUE_FLUSH, None, None)
        except:
            print("Ses motoru başlatılamadı.")

    def jarvis_islem(self, instance):
        soru = self.input_box.text
        self.input_box.text = ""
        
        # Basit Öğrenme Mantığı (API kullanmadan)
        # Buraya kendi "Soru-Cevap" veritabanınızı oluşturabilirsiniz
        cevaplar = {
            "merhaba": "Merhaba efendim, sistemler aktif.",
            "nasılsın": "Çekirdek sıcaklığım normal, sizin için buradayım.",
            "feneri aç": "Işık protokolü tetiklendi.",
            "kimsin": "Ben sizin tarafınızdan geliştirilen Jarvis Core yazılımıyım."
        }
        
        yanit = cevaplar.get(soru.lower(), "Bunu henüz öğrenmedim efendim, hafızama kaydediyorum.")
        self.status.text = yanit
        self.sesli_konus(yanit)

if __name__ == "__main__":
    JarvisApp().run()
