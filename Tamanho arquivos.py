import os, shutil
os.chdir('C:\\Users\\Lina\\')
for folderName, subfolders, filenames in os.walk('C:\\Users\\Lina'):
     for filename in os.listdir('C:\\Users\\Lina'):
        totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\Lina', filename))