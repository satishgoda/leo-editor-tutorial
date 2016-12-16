<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="sgoda.20161216175419.2" a="E"><vh>\@button Promoting Child Bodies</vh>
<v t="sgoda.20161216175941.1"><vh>original example</vh></v>
<v t="sgoda.20161216175744.1"><vh>promote-child-bodies</vh></v>
</v>
<v t="sgoda.20161216175451.1" a="E"><vh>Book</vh>
<v t="sgoda.20161216175459.1"><vh>Chapter 1</vh></v>
<v t="sgoda.20161216175506.1"><vh>Chapter 2</vh></v>
<v t="sgoda.20161216175515.1"><vh>Chapter 3</vh></v>
<v t="sgoda.20161216175521.1"><vh>Chapter 4</vh></v>
</v>
<v t="sgoda.20161216175847.1" a="E"><vh>Book</vh>
<v t="sgoda.20161216175847.2"><vh>Chapter 1</vh></v>
<v t="sgoda.20161216175847.3"><vh>Chapter 2</vh></v>
<v t="sgoda.20161216175847.4"><vh>Chapter 3</vh></v>
<v t="sgoda.20161216175847.5"><vh>Chapter 4</vh></v>
</v>
<v t="sgoda.20161216180500.1" a="E"><vh>Book</vh>
<v t="sgoda.20161216180500.2"><vh>Chapter 1</vh></v>
<v t="sgoda.20161216180500.3"><vh>Chapter 2</vh></v>
<v t="sgoda.20161216180500.4"><vh>Chapter 3</vh></v>
<v t="sgoda.20161216180500.5"><vh>Chapter 4</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="sgoda.20161216175419.2">@language rest

This file is based on the information available at the link below.

http://leoeditor.com/scripting-miscellany.html#button-example</t>
<t tx="sgoda.20161216175451.1">@language rest

This is My Book
===============</t>
<t tx="sgoda.20161216175459.1">Chapter 1
---------</t>
<t tx="sgoda.20161216175506.1">Chapter 2
---------</t>
<t tx="sgoda.20161216175515.1">Chapter 3
---------</t>
<t tx="sgoda.20161216175521.1">Chapter 4
---------</t>
<t tx="sgoda.20161216175744.1">@language python

result = [p.b]

b = c.undoer.beforeChangeNodeContents(p)

for child in p.children():
    if child.b:
        result.append('\n%s\n' % (child.b))
    else:
        g.es("{0} does not have a body".format(child.h))

p.b = ''.join(result)

c.undoer.afterChangeNodeContents(p, 'promote-child-bodies', b)</t>
<t tx="sgoda.20161216175847.1">@language rest

This is My Book
===============
Chapter 1
---------

Chapter 2
---------

Chapter 3
---------

Chapter 4
---------</t>
<t tx="sgoda.20161216175847.2">Chapter 1
---------</t>
<t tx="sgoda.20161216175847.3">Chapter 2
---------</t>
<t tx="sgoda.20161216175847.4">Chapter 3
---------</t>
<t tx="sgoda.20161216175847.5">Chapter 4
---------</t>
<t tx="sgoda.20161216175941.1">@language python

result = [p.b]

b = c.undoer.beforeChangeNodeContents(p)

for child in p.children():
    if child.b:
        result.append('\n- %s\n\n%s\n' % (child.h,child.b))
    else:
        result.append('\n- %s\n\n' % (child.h))

p.b = ''.join(result)

c.undoer.afterChangeNodeContents(p,'promote-child-bodies',b)</t>
<t tx="sgoda.20161216180500.1">@language rest

This is My Book
===============
Chapter 1
---------

Introduction to Leo

Chapter 2
---------

Leo use cases

Chapter 3
---------

Basic scripting in Leo

Chapter 4
---------

Advanced scripting in Leo
</t>
<t tx="sgoda.20161216180500.2">Chapter 1
---------

Introduction to Leo</t>
<t tx="sgoda.20161216180500.3">Chapter 2
---------

Leo use cases</t>
<t tx="sgoda.20161216180500.4">Chapter 3
---------

Basic scripting in Leo</t>
<t tx="sgoda.20161216180500.5">Chapter 4
---------

Advanced scripting in Leo</t>
</tnodes>
</leo_file>
