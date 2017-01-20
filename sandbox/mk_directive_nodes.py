@language python

import os

cwd = os.getcwd()

if p.h.startswith('@button'):
    raise ValueError("Watch what you click!")

copied_p = p.copy()

child_names = [child.h for child in p.children()]

for line in sorted(os.listdir(cwd)):
    if line in child_names:
       g.es("Already exists: {0}".format(line), color='red')
       continue

    if line.startswith('.'):
        continue

    child = copied_p.insertAsLastChild()

    if os.path.isfile(line):
        node_pfx = '@@edit'
        
        if line.endswith(".py"):
            node_pfx = '@@clean'
        elif line.endswith('.png'):
            node_pfx = '@image'
        elif line.endswith('.mp4'):
            node_pfx = '@movie'
        child.h = '{0} {1}'.format(node_pfx, line)
    elif os.path.isdir(line):
        child.h = line
        child.b = "@path {0}".format(line)

c.redraw()
