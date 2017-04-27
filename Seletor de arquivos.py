import os, shutil
os.chdir('C:\\Users\\Lina\\Downloads\\')
a="jpg"
b="pdf"
for folderName, subfolders, filenames in os.walk('C:\\Users\\Lina\\Downloads\\'):
    for filename in filenames:
        k=filename
        t=k[-3]+k[-2]+k[-1]
        if t==b:
            shutil.move(os.path.join(folderName+"\\"+filename),'C:\\Users\\Lina\\Desktop\\PDF')
        if t==a:
            shutil.move(os.path.join(folderName+"\\"+filename),'C:\\Users\\Lina\\Desktop\\JPG')
                    
             
            
            
