Wed, Nov 01, 2017
===============

Back to Leo blogging. It has been a while since I used Leo, but today I had to dig it up to solve a problem at hand.

button-dirview-vim::
   @language python

   import os

   os.system("gvim {0}".format('./'))


Tue, Dec 27, 2016
===============

* https://github.com/satishgoda/leo-editor-tutorial/blob/master/sandbox/mute_clean_nodes.py
* https://github.com/satishgoda/leo-editor-tutorial/blob/master/sandbox/load_modules.py

Fri, Dec 23, 2016
===============

**Mapping file system directories to outline nodes**

*map_fs_dirs_to_onodes.py*::

  @path apps

  @language python

  import os

  childrenNames = [p.h for p in p.children()]

  copied_p = p.copy()

  def nodeCreationStatus(nodeName, status, color):
      msg = 'Node {0} {1}'.format(nodeName, status)
      g.es(msg, color=color)

  appNames = sorted(os.listdir('./'))

  for appName in appNames:
      if appName in childrenNames:
          nodeCreationStatus(appName, 'already exists', 'red')
          continue

      appNode = copied_p.insertAsLastChild()

      appNode.h = appName
      appNode.b = '@path ' + appName

      nodeCreationStatus(appName, 'created', 'green')

  c.redraw_now()

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
