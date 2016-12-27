import os

cwd = os.getcwd()

for item in os.listdir('.'):
    suffix = ''
    
    if os.path.isdir(item):
        suffix = '/'
    
    fitem = "{0}{1}".format(item, suffix)
    
    g.es(fitem)

g.es(cwd)
