from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout


class MyApp(App):
    Config.set("graphics", "width", 600)
    Config.set("graphics", "height", 600)
    Config.set("graphics", "resizable", 0)

    def build(self):
        self.knopka = Button()

        gl = GridLayout(cols=3)
        gl.add_widget(self.knopka)
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        gl.add_widget(Button())
        return gl

    def callback_press(self, instance):
        instance.text = "ваш любимый текст"

if __name__ == '__main__':
    MyApp().run()
