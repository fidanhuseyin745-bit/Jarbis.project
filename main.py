import urllib.request
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
from jnius import autoclass

class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()
        
        # Hafızadaki varsayılan cevaplar
        self.hafiza = {
            "selam": "Merhaba efendim.",
            "durum": "Sistemler stabil."
        }

        # 1. DÖNEN HOLOGRAM
        self.hologram = Image(source='jarvis.png', pos_hint={'center_x': 0.5, 'center_y': 0.55}, size_hint=(0.75, 0.75))
        self.layout.add_widget(self.hologram)

        # 2. DURUM PANELİ
        self.status = Label(text="Jarvis Çekirdek Aktif.", pos_hint={'center_x': 0.5, 'center_y': 0.22}, color=(0, 1, 1, 1))
        self.layout.add_widget(self.status)

        # 3. GİRİŞ KUTUSU
        self.input_box = TextInput(hint_text='Emir bekleniyor...', size_hint=(0.8, 0.06), pos_hint={'center_x': 0.5, 'center_y': 0.1}, background_color=(0,0,0,0.7), foreground_color=(0,1,1,1), multiline=False)
        self.input_box.bind(on_text_validate=self.islem_yap)
        self.layout.add_widget(self.input_box)

        # AÇILIŞTA GÜNCELLEMEYİ BAŞLAT
        Clock.schedule_once(self.buluttan_ogren, 2)
        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def buluttan_ogren(self, dt):
        # BURASI ÖNEMLİ: Kendi GitHub kullanıcı adınızı "Huseyin" yazan yere yazın
        # GitHub'da 'komutlar.txt' diye bir dosya açıp içine selam:merhaba gibi yazacağız
        url = "https://raw.githubusercontent.com/Huseyin/jarvis/main/komutlar.txt"
        try:
            response = urllib.request.urlopen(url)
            data = response.read().decode('utf-8')
            # Gelen veriyi hafızaya ekle (Örn: "naber:iyiyim,fener:açıldı")
            for line in data.split(','):
                k, v = line.split(':')
                self.hafiza[k.strip().lower()] = v.strip()
            self.status.text = "Yeni protokoller başarıyla indirildi."
            self.sesli_konus("Sistem güncellendi efendim.")
        except:
            self.status.text = "Bulut bağlantısı kurulamadı."

    def sesli_konus(self, mesaj):
        try:
            Locale = autoclass('java.util.Locale')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.tts.setLanguage(Locale.getDefault())
            self.tts.speak(mesaj, TextToSpeech.QUEUE_FLUSH, None, None)
        except: pass

    def islem_yap(self, instance):
        soru = self.input_box.text.lower()
        self.input_box.text = ""
        
        yanit = self.hafiza.get(soru, "Bu komut hafızamda yok efendim.")
        self.status.text = yanit
        self.sesli_konus(yanit)

if __name__ == "__main__":
    JarvisApp().run()
