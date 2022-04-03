import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


main = Gtk.main
main_quit = Gtk.main_quit


class Window(Gtk.Window):
    """Gtk.Window doc:
    http://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window
    """
    def __init__(
            self, title="title",
            subtitle="",
            icon='sgIcon',
            header_bar=True,
            is_main=True,
            show=True,
            base_dir=None,
            **kwargs,
            ):
        Gtk.Window.__init__(self)
        self.set_size_request(800, 600)
        self.scroll = Gtk.ScrolledWindow()
        self.add(self.scroll)
        self.viewport = Gtk.Viewport()
        self.scroll.add(self.viewport)
        self.main_box = Gtk.VBox()
        self.viewport.add(self.main_box)
        # Header Bar
        if header_bar:
            self.header_bar = Gtk.HeaderBar()
            self.header_bar.set_show_close_button(True)
            self.header_bar.set_title(title)
            self.header_bar.set_subtitle(subtitle)
            self.set_titlebar(self.header_bar)
        else:
            self.set_title(title)
        # Icon
        if base_dir:
            self.base_dir = base_dir
            if icon:
                icon_path = os.path.join(self.base_dir, icon)
                self.set_icon_from_file(icon_path)

        # window itself
        if is_main:
            self.connect("delete-event", Gtk.main_quit)
        if show:
            self.show_all()
