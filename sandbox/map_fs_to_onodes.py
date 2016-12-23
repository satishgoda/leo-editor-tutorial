@path apps
@language python

import os
import glob

def nodeCreationStatus(nodeName, status, color):
    msg = 'Node {0} {1}'.format(nodeName, status)
    g.es(msg, color=color)

def createNodes(appNames, childrenNames, position):
    for appName in appNames:
        if appName in childrenNames:
            nodeCreationStatus(appName, 'already exists', 'red')
            continue
    
        child = position.insertAsLastChild()
        
        child.h = appName
        child.b = '@path ' + appName
        
        nodeCreationStatus(appName, 'created', 'green')

def updateChildNode(child):
    ##files = os.listdir(child.h)
    files = glob.glob(child.h + '/*.py')
    position = child.copy()
    for fileName in files:
        fileNode = position.insertAsLastChild()
        fileNode.h = '@clean {0}'.format(fileName.split('/')[-1])

position = p.copy()
    
appNames = sorted(os.listdir('./'))
childrenNames = [position.h for position in position.children()]

#createNodes(appNames, childrenNames, position)

##position = p.copy()
##for child in position.children():

#for child in p.children():
#    updateChildNode(child)

for child in p.children():
    #child.h = '@' + child.h
    #child.h = child.h[1:]
    for cchild in child.children():
        cchild.h = '@' + cchild.h

c.redraw_now()
