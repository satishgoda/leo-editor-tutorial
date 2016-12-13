"""
This script is supposed to be run from within Leo.

Select the script node and then click on the "script-button" button to create a clickable button.

Select a outline node under which the chapter nodes must be created.
Click on the button generated for this script.
"""

from urllib import urlopen
from HTMLParser import HTMLParser


class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False

VOLUME = 'II'
TOTAL_CHAPTERS = 42
URL = "http://www.feynmanlectures.caltech.edu/{0}_{1:02}.html"

copied_position = p.copy()

for index in range(1, TOTAL_CHAPTERS+1):
    new_node = copied_position.insertAsLastChild()
    FULLURL = URL.format(VOLUME, index)
    new_node.b = FULLURL
    html_string = str(urlopen(FULLURL).read())
    parser = TitleParser()
    parser.feed(html_string)
    title = parser.title
    chapter_name = title.split(':')[-1].strip()
    new_node.h = "@chapter {0} Chapter {1:02} - {2}".format(VOLUME, index, chapter_name)
    g.es(chapter_name)

c.redraw_now()
