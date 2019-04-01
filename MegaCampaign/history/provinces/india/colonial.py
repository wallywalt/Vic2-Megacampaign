import glob
import os.path

save_path ='C:/Users/Kim/Desktop/Test/Save'

for file in glob.glob("*.txt"):
    if 'owner=FRA' or 'owner=X03' in open(file).read():
        completeName = os.path.join(save_path, file)
        with open(completeName,"a") as myfile:
                myfile.write('colonial=2')
    

            
