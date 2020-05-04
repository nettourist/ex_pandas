# -*- coding: utf-8 -*-
# -*- vk.com/nettourist -*-
import pandas as pd

default = pd.read_excel (r'data/default.xlsx')
keys = pd.read_excel (r'data/keys.xlsx')

while True:
    search = input('[1] Default\n[2] Keys\nPress: ')
    if search in ['1']:
        print (default)

    if search in ['2']:
        print (keys)
