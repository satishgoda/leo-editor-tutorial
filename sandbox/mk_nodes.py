@language python

if p.h.startswith('@button'):
    raise ValueError("This script cannot be used on button nodes")

if not p.b.split():
    raise Exception("""For creating children for the selected node
    The body of the seelcted node must contain the name of the child 
    specified one per line.
    """)

copied_p = p.copy()

child_names = (child.h for child in p.children())

URL_BASE = "https://github.con/satishgoda/{0}"

for line in p.b.split():
    if not line:
        continue

    if line in child_names:
        g.es("Already exists: {0}".format(line), color='red')
        continue

    child = copied_p.insertAsLastChild()
    child.h = line
    child.b = URL_BASE.format(line)

c.redraw()
