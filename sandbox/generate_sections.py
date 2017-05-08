@language python

import leo

copied_position = p.copy()

#g.es(type(copied_position))

#g.es(isinstance(copied_position, leo.core.leoNodes.Position))


lines = copied_position.b.split('\n')

class NewNode(object):
    def __init__(self, parent, heading):
        self._parent = parent
        self.addNode(heading)
    
    def addNode(self, heading):
        node = self.parent.insertAsLastChild()
        node.h = heading
    
    @property
    def parent(self):
        parent = self._parent
        while True:
            if isinstance(parent, leo.core.leoNodes.Position):
                return parent
            parent = parent._parent

for line in lines:
    parts = line.split(':')
    
    if len(parts) < 2:
        continue
    
    first, rest = map(unicode.strip, (parts[0], parts[1]))
    
    if first.startswith('Section'):
        section_node = NewNode(copied_position, rest)
    elif first.startswith('Video'):
        video_node = NewNode(section_node, rest)

c.redraw_now()
