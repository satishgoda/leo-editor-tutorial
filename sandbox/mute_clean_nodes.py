import os
import glob

position = p.copy()

for child in position.children():
    h = child.h
    child.h = '@' + h

c.redraw_now()
