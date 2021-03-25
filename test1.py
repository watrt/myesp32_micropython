import os
l=os.listdir()
for f in l:
    s=os.stat(f)
    print('{0},{1},{2}'.format(f, s[0], s[6]))
