from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem, ImageLeftWidget
from kivymd.uix.list import MDList

class SelfInventoryScreen(MDScreen):
    def __init__(self, pokemons, **kwargs):
        super(SelfInventoryScreen, self).__init__(**kwargs)
        self.main_layout = GridLayout()
        self.main_layout.cols = 1
        self.main_layout.spacing = 40
        self.main_layout.add_widget(MDLabel(text='Inventário', valign='top', halign='center', font_style='H4'))
        self.pokemons = pokemons
        self.layout = MDList()
        self.scroll = ScrollView(size_hint=(1, None), size=(200, 350))
        for pokemon in self.pokemons:
            self.item = OneLineIconListItem(text=pokemon['pokemon_name'])
            self.item.add_widget(ImageLeftWidget(source=pokemon['pokemon_image']))
            self.layout.add_widget(self.item)
        if(self.pokemons == []):
            self.layout.add_widget(MDLabel(text='Vish, você não tem mais pokemóns', halign='center', font_style='Subtitle1'))
        self.scroll.add_widget(self.layout) 
        self.main_layout.add_widget(self.scroll)
        self.add_widget(self.main_layout)