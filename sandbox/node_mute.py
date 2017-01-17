## @button node_mute @color=magenta
## @language python

if p.h.startswith('@'):
    p.h = '@' + p.h

c.redraw_now()
