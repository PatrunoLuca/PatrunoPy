from json import dump, load
from random import choice

import certifi
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.snackbar import Snackbar


class Content(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.container = self.ids.container
    
    def adding(self, dict):
        for i in reversed(dict["cronologia"]):
            haiku = list(dict["cronologia"][i].values())
            self.container.add_widget(SwipeToDeleteItem(text=haiku[0], secondary_text=haiku[1], tertiary_text=haiku[2], number=i))

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()
    number = StringProperty()
        
    

class HaikuGenerator(MDApp):

    info_dialog = None
    contact_dialog = None
    history_dialog = None
    
    def build(self):
        self.title = "Haiku Generator"
        with open('haiku.json', 'r') as outfile:
            self.database = load(outfile)
        self.theme_cls.theme_style =  self.database["tema"]
        if self.theme_cls.theme_style == "Dark":
            self.title_color = "ffffff"
            self.text_color = "cccccc"
        elif self.theme_cls.theme_style == "Light":
            self.title_color = "000000"
            self.text_color = "181818"
        self.theme_cls.primary_palette = "Blue"
        self.icon = 'loghino.png'
        return Builder.load_file("Haiku.kv")

    def generate_haiku(self):
        with open('haiku.json', 'r') as outfile:
            self.root.ids["verso_1"].text = choice(self.database['verso_1'])
            self.root.ids["verso_2"].text = choice(self.database['verso_2'])
            self.root.ids["verso_3"].text = choice(self.database['verso_3'])
        self.add_to_history()

    def copy_haiku(self):
        haiku = [self.root.ids["verso_1"].text, self.root.ids["verso_2"].text, self.root.ids["verso_3"].text]
        if haiku != ["", "", ""] and  "\n".join(haiku) != Clipboard.paste():
            Clipboard.copy("\n".join(haiku))
            Snackbar(text=f"[color={self.text_color}]Elemento copiato negli appunti![/color]",).show()
        
    def show_info_dialog(self):
        app_info = "L'applicazione è stata sviluppata da un gruppo di studenti dell'istituto \"Gian Battista Vico\", all'indirizzo Coding, in un progetto scolastico monitorato in compresenza dalla professoressa di Italiano Luciana Soravia e il professore di coding Diomede Mazzone."
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title = f"[color={self.title_color}]Informazioni App[/color]",
                text = f"[color={self.text_color}]{app_info}[/color]",
                buttons=[
                    MDFlatButton(
                        text = "ESCI", 
                        text_color = self.theme_cls.primary_color,
                        on_release = self.close_info_dialog
                        )],
                auto_dismiss = True,
                size_hint = (0.8, 1)
            )
        self.info_dialog.open()

    def show_contact_dialog(self):
        app_info = "Barile Luigi:\n     barile.luigi.s03@liceoviconapoli.it\n\nPatruno Luca:\n     patruno.luca.s26@liceoviconapoli.it\n\nRipoli Luca:\n     ripoli.luca.s13@liceoviconapoli.it\n\nSenese Walter:\n     senese.walter.s30@liceoviconapoli.it"
        if not self.contact_dialog:
            self.contact_dialog = MDDialog(
               title = f"[color={self.title_color}]I Nostri Contatti[/color]",
                text = f"[color={self.text_color}]{app_info}[/color]",
                buttons=[
                    MDFlatButton(
                        text = "ESCI", 
                        text_color = self.theme_cls.primary_color,
                        on_release = self.close_contact_dialog
                        )],
                auto_dismiss = True,
                size_hint = (0.8, 1)
            )
        self.contact_dialog.open()

    def show_history_dialog(self):
        if not self.history_dialog:
            self.history_container = Content()
            self.history_container.adding(self.database)
            self.history_dialog = MDDialog(
                type="custom",
                title = f"[color={self.title_color}]Cronologia[/color]",
                content_cls = self.history_container,
                buttons = [
                    MDFlatButton(
                        text = "ESCI", 
                        text_color = self.theme_cls.primary_color,
                        on_release = self.close_history_dialog
                        ),
                    MDFlatButton(
                        text = "CANCELLA CRONOLOGIA", 
                        text_color = self.theme_cls.primary_color,
                        on_release = self.delete_history
                        )],
                auto_dismiss = True,
                size_hint = (0.8, 1)
            )
        self.history_dialog.open()

    def close_info_dialog(self, obj):
        self.info_dialog.dismiss()

    def close_contact_dialog(self, obj):
        self.contact_dialog.dismiss()

    def close_history_dialog(self, obj):
        self.history_dialog.dismiss()
        self.history_dialog = None
        self.reload_history()

    def change_theme(self): 
        with open('haiku.json', 'w') as outfile:
            self.database["tema"] = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
            dump(self.database, outfile,  indent=4, sort_keys=True)
        self.theme_cls.theme_style =  self.database["tema"]
        if self.theme_cls.theme_style == "Dark":
            self.title_color = "ffffff"
            self.text_color = "cccccc"
        elif self.theme_cls.theme_style == "Light":
            self.title_color = "000000"
            self.text_color = "181818"
        Snackbar(text=f"[color={self.text_color}]Il tema è stato modificato![/color]").show()
        
        self.info_dialog = None
        self.contact_dialog = None
        self.history_dialog = None

    def add_to_history(self):
        with open('haiku.json', 'w') as outfile:
            self.database["cronologia"]["elem_%s" % (len(self.database["cronologia"].keys()) + 1)] = {
                "verso_1" : self.root.ids["verso_1"].text,
                "verso_2" : self.root.ids["verso_2"].text,
                "verso_3" : self.root.ids["verso_3"].text
                }
            dump(self.database, outfile, indent=4, sort_keys=True)
        self.history_dialog = None
        self.reload_history()

    def reload_history(self):
        new_history = {}
        for i in enumerate(self.database["cronologia"].values(), start=1):
            new_history["elem_%s" % i[0]] = i[1]
        with open('haiku.json', 'w') as outfile:
            self.database["cronologia"] = new_history
            dump(self.database, outfile, indent=4, sort_keys=True)
    
    def delete_history(self, obj):
        with open('haiku.json', 'w') as outfile:
            self.database["cronologia"] = {}
            dump(self.database, outfile, indent=4, sort_keys=True)
        self.close_history_dialog("")
        self.history_dialog = None
        self.reload_history()
        Snackbar(text=f"[color={self.text_color}]La cronologia è stata eliminata![/color]").show()
    
    def copy_item(self, obj):
        haiku = [obj.text, obj.secondary_text, obj.tertiary_text]
        if haiku != ["", "", ""] and  "\n".join(haiku) != Clipboard.paste():
            Clipboard.copy("\n".join(haiku))
            Snackbar(text=f"[color={self.text_color}]Elemento copiato negli appunti![/color]").show()
    
    def delete_item(self, obj):
        with open('haiku.json', 'w') as outfile:
            del self.database['cronologia'][obj.number]
            dump(self.database, outfile, indent=4, sort_keys=True)
        self.history_container.container.remove_widget(obj)
        Snackbar(text=f"[color={self.text_color}]Elemento eliminato dalla cronologia![/color]").show()
        

if __name__ == '__main__':
    __version__ = "1.0"
    Window.size = (500,500)
    Application = HaikuGenerator()
    Application.run()
