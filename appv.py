from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Olá, Kivy!")
        btn = Button(text="Clique aqui")
        btn.bind(on_press=self.mudar_texto)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def mudar_texto(self, instance):
        self.label.text = "Você clicou!"

MeuApp().run()