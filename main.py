import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
from jnius import autoclass

class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        self.layout = FloatLayout()
        
        # Kodların saklanacağı dosya yolu
        self.kod_dosyasi = os.path.join(self.user_data_dir, "ozel_mantik.py")
        self.hafiza = {"selam": "Merhaba Hüseyin bey, sistem hazır."}

        # 1. DÖNEN HOLOGRAM
        self.hologram = Image(source='jarvis.png', pos_hint={'center_x': 0.5, 'center_y': 0.55}, size_hint=(0.7, 0.7))
        self.layout.add_widget(self.hologram)

        # 2. ANA EKRAN YAZISI
        self.status = Label(text="Sistem Aktif", pos_hint={'center_x': 0.5, 'center_y': 0.2}, color=(0, 1, 1, 1))
        self.layout.add_widget(self.status)

        # 3. GİZLİ EDİTÖR PANELİ (Başlangıçta kapalı)
        self.editor = TextInput(
            text="selam:Merhaba efendim\nnaber:İyiyim siz nasılsınız?",
            size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6},
            visible=False, opacity=0
        )
        self.layout.add_widget(self.editor)

        # 4. GÜNCELLE/KAYDET BUTONU (Gizli)
        self.save_btn = Button(
            text="SİSTEMİ GÜNCELLE", size_hint=(0.9, 0.1), 
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            opacity=0, disabled=True
        )
        self.save_btn.bind(on_press=self.kodu_kaydet)
        self.layout.add_widget(self.save_btn)

        # 5. PANELİ AÇMA BUTONU (Sağ üstte küçük şeffaf bir yer)
        self.admin_btn = Button(text="ADM", size_hint=(0.1, 0.05), pos_hint={'right': 1, 'top': 1}, background_color=(0,0,0,0.1))
        self.admin_btn.bind(on_press=self.paneli_ac_kapat)
        self.layout.add_widget(self.admin_btn)

        # 6. KOMUT GİRİŞİ (Normal kullanım için)
        self.input_box = TextInput(hint_text='Komut...', size_hint=(0.8, 0.06), pos_hint={'center_x': 0.5, 'center_y': 0.1}, multiline=False)
        self.input_box.bind(on_text_validate=self.cevap_ver)
        self.layout.add_widget(self.input_box)

        Clock.schedule_interval(self.dondur, 1.0 / 60.0)
        return self.layout

    def dondur(self, dt):
        self.hologram.rotation += 1

    def paneli_ac_kapat(self, instance):
        if self.editor.opacity == 0:
            self.editor.opacity = 1
            self.save_btn.opacity = 1
            self.save_btn.disabled = False
        else:
            self.editor.opacity = 0
            self.save_btn.opacity = 0
            self.save_btn.disabled = True

    def kodu_kaydet(self, instance):
        # Editöre yazdığınız satırları hafızaya alır
        yeni_kod = self.editor.text
        for line in yeni_kod.split('\n'):
            if ":" in line:
                k, v = line.split(':')
                self.hafiza[k.strip().lower()] = v.strip()
        self.status.text = "Sistem Dahili Olarak Güncellendi!"
        self.paneli_ac_kapat(None) # Paneli kapat

    def cevap_ver(self, instance):
        soru = self.input_box.text.lower()
        self.input_box.text = ""
        yanit = self.hafiza.get(soru, "Bu komut henüz tanımlanmadı.")
        self.status.text = yanit

if __name__ == "__main__":
    JarvisApp().run()
