import os, shutil
os.chdir('C:\\Users\\UFU\\Desktop\\Corel\\CorelDRAW Graphics Suite X7 - 64 Bits')
a=200000000
for folderName, subfolders, filenames in os.walk('C:\\Users\\UFU\\Desktop\\Corel\\CorelDRAW Graphics Suite X7 - 64 Bits'):
    for filename in filenames:
       p=os.path.getsize(os.path.join(folderName+"\\", filename))           
       if p>=a:
            print("Arquivo maior que 200Mb \n "+ folderName+filename)
            
            

        
