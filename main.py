#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import sillyGtk as sg


# Here some callbacks
def callback_plus(*args):
    print('Plus')


def callback_options(*args):
    print('Options')


# optional indicator
indicator = sg.Indicator(
    icon='sgIcon',  # required
    label='label example',
    menu_items=[
        ("Plus", callback_plus),
        "_separator",
        ("Options", callback_options),
    ]
)

# window
# window = sg.Window('Super app', icon=None)

sg.main()
