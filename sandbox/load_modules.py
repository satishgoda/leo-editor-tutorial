import os
import glob

position = p.copy()

for module_name in position.b.split():
    fileNode = position.insertAsLastChild()
    fileNode.h = '@clean {0}.py'.format(module_name)

c.redraw_now()

"""
DependencyNodeUI
ComputeNodeUI
RandomUI
ExpressionUI
BoxUI
ReferenceUI
BackdropUI
DotUI
SubGraphUI
SwitchUI
ContextVariablesUI
TimeWarpUI
LoopUI
AnimationUI
"""
