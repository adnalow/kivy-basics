from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class MainApp(App):
    def build(self):
       layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
       btn = Button(text='Button1')
       btn2 = Button(text='Button2')
       btn3 = Button(text='Button3')
       layout.add_widget(btn)
       layout.add_widget(btn2)
       layout.add_widget(btn3)
       return layout
        
MainApp().run()