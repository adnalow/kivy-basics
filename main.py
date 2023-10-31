from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class MainApp(App):
    def build(self):
        # img = Image(source='sdasd.png')
        img = AsyncImage(source='https://static.vecteezy.com/system/resources/previews/024/029/752/original/house-icon-clipart-transparent-background-free-png.png')
        return img
        
        
    
MainApp().run()