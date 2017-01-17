
## @button node_unmute @color=green
## @language python

if p.h.startswith('@@'):
    p.h = p.h[1:]

c.redraw_now()
