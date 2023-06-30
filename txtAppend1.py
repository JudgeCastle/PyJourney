import os

old_files = os.listdir('path')
new_files = 'path'

for file in old_files:
    os.rename('path' + file, new_files + file + '.extension')