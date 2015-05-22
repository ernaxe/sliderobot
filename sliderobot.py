from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
import main

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    store_input_folder = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(BoxLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(store_input_folder=self.store_input_folder, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def store_input_folder(self, path, filename):
        print path
        print filename
        self.selected_folder.text = os.path.join(path) + "/"
        self.dismiss_popup()

    def process(self):
        fd = self.selected_folder.text
        fdout = fd+"cropped/"
        top = int(self.coord_top.text)
        bottom = int(self.coord_bottom.text)
        left = int(self.coord_left.text)
        right = int(self.coord_right.text)
        nrow = int(self.slide_rows.text)
        ncol = int(self.slide_cols.text)
        main.crop_and_add_to_slide(fd,fdout,top,bottom,left,right,nrow,ncol)


class Sliderobot(App):
    pass

Factory.register('Root', cls=Root)
#Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Sliderobot().run()
