from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IconLeftWidget, IconRightWidget,ThreeLineAvatarIconListItem

from controllers.BarterSolicitationController import BarterSolicitationController

class BarterSolicitationScreen(Screen):
    def __init__(self, barter_solicitations, **kwargs):
        super(BarterSolicitationScreen, self).__init__(**kwargs)
        self.barter_solicitations = barter_solicitations
        
        self.mainLayout = GridLayout()
        self.mainLayout.cols = 1
        self.mainLayout.spacing = 40
        self.mainLayout.add_widget(MDLabel(text='Solicitações de troca', valign='top', halign='center', font_style='H4'))
        self.layout = GridLayout(padding=[100, 0, 100, 0])
        self.layout.cols = 1
        self.layout.spacing = 1
        self.layout.size_hint_y=None
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.scroll = ScrollView(size_hint=(1, None), size=(200, 350))
        
        for barter_solicitation in self.barter_solicitations:
            self.item = ThreeLineAvatarIconListItem(text=f'{barter_solicitation.sender_user_name} te solicitou uma troca', secondary_text= f'O seu {barter_solicitation.want_pokemon_name}', tertiary_text=f'Pelo {barter_solicitation.give_pokemon_name} dele')
            self.item.add_widget(IconLeftWidget(icon='swap-horizontal-circle-outline'))
            self.item_icon1 = IconRightWidget(icon='check-circle-outline')
            self.item_icon1.bind(on_release=lambda x: BarterSolicitationController.on_barter_accepted(self, barter_solicitation.id))
            self.item.add_widget(self.item_icon1)
            self.item_icon = IconRightWidget(icon='cancel')
            self.item_icon.bind(on_release=lambda x: BarterSolicitationController.on_barter_refused(self, barter_solicitation.id))
            self.item.add_widget(self.item_icon)
            self.layout.add_widget(self.item)
        self.scroll.add_widget(self.layout)
        self.mainLayout.add_widget(self.scroll)
        self.add_widget(self.mainLayout)