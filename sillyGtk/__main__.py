import sys


HELP = (
    """
========================= SillyGtk ===================================
SillyGtk is based on PyGobject.
It is basically a collection of pre-set and pre-built Gtk objects.

The purpose is to build interfaces faster and easyer. You can still
adjust precisely your settings and mix sillyGtk with PyGobject.
Most sillyGtk objects are heriting from the Gtk object of the same name.
ex: sillyGtk.Window is heriting from Gtk.Window

usefull PyGobject api documentation here:
http://lazka.github.io/pgi-docs/index.html#Gtk-3.0

OPTIONS:
python3 -m sillyGtk [option]

options are:
-'', '-h', '--help' : display this help


    """
)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(HELP)
    if len(sys.argv) > 1:
        if sys.argv[1] in ('--help', '-h'):
            print(HELP)
