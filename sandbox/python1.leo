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
<v t="sgoda.20161216144140.2" a="E"><vh>@clean python1.py</vh>
<v t="sgoda.20161216145258.1"><vh>&lt;&lt; shebang &gt;&gt;</vh></v>
<v t="sgoda.20161216145409.1"><vh>&lt;&lt; doc &gt;&gt;</vh></v>
<v t="sgoda.20161216145322.1"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="sgoda.20161216145425.1"><vh>&lt;&lt; classes &gt;&gt;</vh></v>
<v t="sgoda.20161216145419.1"><vh>&lt;&lt; functions &gt;&gt;</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="sgoda.20161216144140.2">@language python
&lt;&lt; shebang &gt;&gt;

&lt;&lt; doc &gt;&gt;

&lt;&lt; imports &gt;&gt;

&lt;&lt; classes &gt;&gt;

&lt;&lt; functions &gt;&gt;

if __name__ == '__main__':
    main()
</t>
<t tx="sgoda.20161216145258.1">#!/usr/bin/env python</t>
<t tx="sgoda.20161216145322.1">import sys</t>
<t tx="sgoda.20161216145409.1">"""
The code in this file was generated from Leo Editor.
"""</t>
<t tx="sgoda.20161216145419.1">def main():
    helloWorld = HelloWorld()
    helloWorld()</t>
<t tx="sgoda.20161216145425.1">class HelloWorld(object):

    def __init__(self, message="Hello World"):
        self._message = message

    @property
    def message(self):
        return self._message

    def __call__(self):
        print(self.message)</t>
</tnodes>
</leo_file>
