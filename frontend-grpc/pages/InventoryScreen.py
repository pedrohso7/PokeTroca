from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, ImageLeftWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField

from controllers.InventoryController import InventoryController
class InventoryScreen(MDScreen):
    def __init__(self, id, name, user_id, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        self.my_pokemons = []
        self.pokemons = []
        self.my_pokemon = {}
        self.pokemon = {}
        if(id != -1 & user_id != -1):
            self.my_pokemons = InventoryController.get_user_inventory(self, user_id)
            self.pokemons = InventoryController.get_user_inventory(self, id)
        self.main_layout = GridLayout()
        self.main_layout.cols = 1
        self.main_layout.spacing = 40
        self.home_toolbar = MDToolbar(title='PokeTroca', icon='git')
        self.home_toolbar.left_action_items = [['arrow-left', InventoryController.on_back_pressed]]
        self.main_layout.add_widget(self.home_toolbar)
        self.name = name
        self.main_layout.add_widget(MDLabel(text='Telas de troca', halign='center', font_style='H4'))
        self.layout_button = MDGridLayout(cols=3, padding=[150, 30, 150, 100], spacing=40)
        self.field1 = MDTextField(hint_text='Você deseja', mode='rectangle')
        self.field2 = MDTextField(hint_text='Em troca de', mode='rectangle')
        self.layout_button.add_widget(self.field1)
        self.layout_button.add_widget(self.field2)
        self.barter_button = MDRaisedButton(text='Fazer troca', on_release=lambda x: InventoryController.create_barter(self, user_id, id, self.field1.text, self.field2.text, self.my_pokemons, self.pokemons))
        self.button_container = MDGridLayout(cols=1, padding=[0, 10, 0, 0])
        self.button_container.add_widget(self.barter_button)
        self.layout_button.add_widget(self.button_container) 
        self.main_layout.add_widget(self.layout_button)
        self.layout_label_scrolls = MDGridLayout(cols=2, spacing=30, padding=[100, 100, 130, 0])
        self.layout_label_scrolls.add_widget(MDLabel(text='Inventário de ' + self.name, halign='center', font_style='Subtitle2'))
        self.layout_label_scrolls.add_widget(MDLabel(text='Seu inventário' , halign='center', font_style='Subtitle2'))
        self.main_layout.add_widget(self.layout_label_scrolls)
        self.layout_scroll = MDGridLayout(cols=2, spacing=30, padding=[100, 100, 100, 0])
        self.layout_scroll.size_hint_y=None
        self.layout_scroll.bind(minimum_height=self.layout_scroll.setter('height'))
        self.layout1 = GridLayout(padding=[0, 0, 40, 0])
        self.layout1.cols = 1
        self.layout1.spacing = 1
        self.layout1.size_hint_y=None
        self.layout1.bind(minimum_height=self.layout1.setter('height'))
        self.layout2 = GridLayout(padding=[0, 0, 40, 0])
        self.layout2.cols = 1
        self.layout2.spacing = 1
        self.layout2.size_hint_y=None
        self.layout2.bind(minimum_height=self.layout2.setter('height'))
        self.scroll1 = ScrollView(size_hint=(1, None), size=(200, 300))
        self.scroll2 = ScrollView(size_hint=(1, None), size=(200, 300))
        for pokemon in self.pokemons:
            item = OneLineIconListItem(text=pokemon.pokemonname)
            item.add_widget(ImageLeftWidget(source=pokemon.pokemonimage))
            self.layout1.add_widget(item)
        for pokemon in self.my_pokemons:
            item = OneLineIconListItem(text=pokemon.pokemonname)
            item.add_widget(ImageLeftWidget(source=pokemon.pokemonimage))
            self.layout2.add_widget(item)
        self.scroll1.add_widget(self.layout1) 
        self.scroll2.add_widget(self.layout2)
        self.layout_scroll.add_widget(self.scroll1) 
        self.layout_scroll.add_widget(self.scroll2) 
        self.main_layout.add_widget(self.layout_scroll)
        self.add_widget(self.main_layout)