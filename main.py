from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('screen.kv')


if __name__=='__main__':
    MainApp().run()