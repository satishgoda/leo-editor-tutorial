@language python

import os

cwd = os.getcwd()

files = os.listdir(cwd)


g.es("\nContents of {0}\n".format(cwd), color='green')
g.es("\n")
# g.es("\n".join(files))

for entry in files:
    color = 'black'
    suffix = ''

    if os.path.isfile(entry):
        color = 'cyan'
    elif os.path.isdir(entry):
        color = 'blue'
        suffix = '/'
    
    if entry.startswith('.'):
        color = 'gray'
    
    g.es("{0}{1}".format(entry, suffix), color=color)

g.es("\n")
