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

        # 1. DÖNEN HOLOGRAM (jarvis.png)
        self.hologram = Image(
            source='jarvis.png', 
            pos_hint={'center_x': 0.5, 'center_y': 0.55}, 
            size_hint=(0.75, 0.75)
        )
        self.layout.add_widget(self.hologram)

        # 2. SİSTEM VERİ PANELİ
        self.info = Label(
            text="STATUS: ONLINE\nUPTIME: ACTIVE\nLEARNING: ENABLED",
            font_size='12sp', color=(0, 1, 1, 0.5),
            pos_hint={'center_x': 0.15, 'center_y': 0.95}
        )
        self.layout.add_widget(self.info)

        # 3. MESAJ GİRİŞ KUTUSU
        self.input_box = TextInput(
            hint_text='Emrinizi buraya yazın...',
            size_hint=(0.8, 0.06),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            background_color=(0, 0, 0, 0.7),
            foreground_color=(0, 1, 1, 1),
            multiline=False
        )
        self.input_box.bind(on_text_validate=self.jarvis_islem)
        self.layout.add_widget(self.input_box)

        # 4. CEVAP EKRANI
        self.status = Label(
            text="Sistem emirlerinizi bekliyor.",
            font_size='18sp',
            color=(1, 1, 1, 0.8),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        self.layout.add_widget(self.status)

        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def sesli_konus(self, mesaj):
        # Android'in kendi sesini (TTS) tetikleyen motor
        try:
            Locale = autoclass('java.util.Locale')
            TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            # Ses motoru başlatılıyor
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.tts.setLanguage(Locale.getDefault())
            self.tts.speak(mesaj, TextToSpeech.QUEUE_FLUSH, None, None)
        except:
            print("Mobil ses hatası.")

    def jarvis_islem(self, instance):
        soru = self.input_box.text
        self.input_box.text = ""
        
        # Titreşim (Onay)
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(100)
        except: pass

        # ÖĞRENME VE YANIT MANTIĞI (Burayı istediğin gibi çoğaltabilirsin)
        veritabani = {
            "selam": "Merhaba efendim, tüm sistemler hazır.",
            "nasılsın": "Çekirdek hızım stabil, sizin için en iyi performansta çalışıyorum.",
            "saat kaç": "Sistem saati kontrol ediliyor, ekranın sol üstüne bakabilirsiniz.",
            "kimsin": "Ben sizin tarafınızdan tasarlanan en gelişmiş Jarvis çekirdeğiyim."
        }
        
        yanit = veritabani.get(soru.lower(), "Bunu veri tabanımda bulamadım ama öğrenmeye çalışıyorum.")
        self.status.text = yanit
        self.sesli_konus(yanit)

if __name__ == "__main__":
    JarvisApp().run()
