#! /usr/bin/env python3
# -*- coding : utf-8 -*-

"""TEMPLATE - Main executable"""


import os

# ====================== Dependencies check ===========================
# With this the dependencies will be automaticly installed at the first
# launch of your application.
# You whant to respect the pep8 ? then move it in the
# "if __name__ == '__main__':" of your main executable.

import pkg_resources
dependencies = [
    'pycairo>=1.21.0',
    'PyGObject>=3.42.0',
    # add your own dependencies here
]
try:
    pkg_resources.require(dependencies)
except pkg_resources.DistributionNotFound:
    os.system('pip install PyGObject')
    # add your needed dependencies installs here

# ===================== end of dependencies check =====================

import silly_gtk as sg


# ==================   Silly GTK - main template  =====================
# This template intends to give some basic elements and explainations,
# just delete those you don't whant, and create some new.
# The parameters marked '# required' are really required, the others are
# shown to let you try different values but are optionnal.

# MUST be in your main executable, some paths will be relative to this:
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# =====================================================================


# Here are some callbacks =============================================
# your app should be MVC designed, this is just an example.
def callback_plus(*args):
    print("Plus")


def callback_options(*args):
    print("Options")


def new_window(*args):
    window = sg.Window(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        title='New window example',
        icon='sgIcon',
        header_bar=False,
        is_main=False,
        )
    # sg.Window inherits from Gtk.Window, so you ca use its methods:
    window.set_size_request(200, 100)
    window.resize(300, 200)
    return window


# Building the interface =========================================
# Indicator
indicator = sg.Indicator(
    base_dir=BASE_DIR,  # required for correct icon behaviour
    icon='sgIcon',  # required
    label='label example',
    menu_items=[
        ("new window", new_window),
        ("Plus", callback_plus),
        ("Options", callback_options),
        "_separator",
    ],
    is_main=True,
)

# window
main_window = sg.Window(
        base_dir=BASE_DIR,  # required for correct icon behaviour
        title='Silly Gtk main window',
        icon='sgIcon',
        header_bar=True,
        is_main=True,
        )


sg.main()  # equal to Gtk.main()
