
Thu, Dec 22, 2016
================

**Converting outline headings to sections**

*make_sections.py*::

  copied_node = p.copy()

  for child in copied_node.children():
      old_header = child.h
      child.h = "<" "<" + old_header + ">" ">"

**Automating a part of the rst documentation for my experiments in gaffer.**

*images.py*::

  copied_position = p.copy()

  count = 1

  for line in p.b.split('\n'):
      if not line.startswith(".. image") :
          continue
      node = copied_position.insertAsLastChild()
      node.h = "image_{0}".format(count)
      count += 1
      node.b = line

  c.redraw_now()


Fri, Dec 16, 2016
==================

Week 1 of learning Leo in depth. Loving it. Cloning nodes is one of the most useful features. I am able to create bookmarks in leoDoc.leo file by cloning the nodes of interest.
