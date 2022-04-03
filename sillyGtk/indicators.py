
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
import os

from sillyGtk.menus import create_menu_item


class Indicator():
    """Indicator is NOT heriting from a Gtk object, but is using it.
    If you whant a cistomized indicator, build it from scratch.
    """
    def __init__(self, icon='sgIcon', name="sgApp", menu_items=[], label=None):
        self.app_name = name
        self.iconpath = os.path.abspath(icon)
        print(f"iconpath: {self.iconpath}")
        self.menu_items = menu_items

        # Attributes must be defined before this_
        self.indicator = AppIndicator3.Indicator.new(
            self.app_name,
            self.iconpath,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        self.indicator.set_menu(self.create_menu())
        if label:
            self.indicator.set_label(label, self.app_name)

    def quit(self, source):
        Gtk.main_quit()

    def create_menu(self):
        self.menu = Gtk.Menu()
        # Quit Item
        self.item_quit = Gtk.ImageMenuItem('Quit')
        self.item_quit.set_image(Gtk.Image.new_from_icon_name(
            "process-stop", Gtk.IconSize(5)))
        self.item_quit.connect('activate', self.quit)
        # Custom Items
        for item in self.menu_items:
            item = create_menu_item(item)
            self.menu.append(item)
        # Finalization
        self.menu.append(self.item_quit)
        self.menu.show_all()
        return self.menu
