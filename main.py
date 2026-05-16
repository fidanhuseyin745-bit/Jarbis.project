from kivy.app import App
from kivy.uix.label import Label
class JarvisApp(App):
    def build(self):
        return Label(text='Merhaba Huseyin Bey, Jarvis Hazir!')
if __name__ == '__main__':
    JarvisApp().run()
