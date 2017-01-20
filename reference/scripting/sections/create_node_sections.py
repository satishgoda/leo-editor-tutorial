##onode @button create_nodesections.py color=yellow
##onode.b.dir.lang @language python

"""
When run on another node with the following script in the body, 
this script creates the section nodes as children of the selected node.

@language javascript
<<requires>>

<<functions>>

<<server>>
"""

copied_p = p.copy()

SECTION_START = "<" + "<"
SECTION_END = ">" + ">"

for line in p.b.split('\n'):
    if line.startswith('@'):
        continue
    if line.startswith(SECTION_START) and line.endswith(SECTION_END):
        h = line.strip(SECTION_START + SECTION_END)
        child = copied_p.insertAsLastChild()
        child.h = SECTION_START + h + SECTION_END

c.redraw_now()
