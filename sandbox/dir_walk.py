import os

cwd = os.getcwd()

for root, dirs, files in os.walk(cwd):
    relrootpath = os.path.relpath(root)
    
    fstr = "{0} (f: {1} d: {2})".format(relrootpath, len(files), len(dirs))
    
    if '.git' in dirs:
        dirs.remove('.git')
    
    g.es(fstr)

g.es(cwd)
