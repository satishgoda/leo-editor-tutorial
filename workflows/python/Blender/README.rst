

Snippet to create @clean nodes for a sub-package

.. code::

  @path bl_ui

  @language python

  import os

  copied_p = p.copy()

  files = os.listdir('E:\\blender\\blender-2.78a-windows64\\2.78\\scripts\\startup\\bl_ui')

  for filename in files:
    if filename in ('__pycache__',):
      continue
    child = copied_p.insertAsLastChild()
    child.h = '@clean {0}'.format(filename)

  c.redraw_now()
