@language python

VOLUME = 'II'
TOTAL_CHAPTERS = 42
URL = "http://www.feynmanlectures.caltech.edu/{0}_{1:02}.html"

copied_position = p.copy()

for index in range(1, TOTAL_CHAPTERS+1):
    new_node = copied_position.insertAsLastChild()
    new_node.h = "@chapter {0} Chapter {1:02} - ".format(VOLUME, index)
    new_node.b = URL.format(VOLUME, index)

c.redraw_now()
