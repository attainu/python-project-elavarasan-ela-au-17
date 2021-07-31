import os 
import shutil
import random
import time
import datetime

print("Welcome To Junk File Organizer")
print("Project developed by elavarasan")
print("Choose your option: ")
print("-------------------------------------------")
print("1 : Orginaze by File Extension")
print("2 : Organize by File Size")
print("3 : Organize by File Date")
print("-------------------------------------------")
typeofsort = input("Enter Organize Method Option: ")
folderpath = input('Enter any Directory path to Sort the Files: ')


# To Organize the file by Extensions

file_extensions={
       'Audio':('.mp3','.wav','.flac', '.m4a', '.aac'),
       'Video':('.mp4','.mkv','.MKV','.flv','.mpeg'),
       'Images':('.jpeg', '.jpg', '.tiff', '.gif', '.png'),
       'Docs':('.doc','.pdf','.txt','.docx','.xls', '.xlsx', '.ppt', '.pptx', '.xps'),
       'Archives':('.zip', '.7z', '.rar'),
       'Others':('.exe', '.apk', '.bat', '.bin'),
       'Programming':('.py', '.htm', '.html', '.html5', '.css', '.php', '.js')
}
new_path={
    "Organized":('Audio','Video','Images','Docs','Archives','Others','Programming')
}

if typeofsort=="1":
    print("File Organizing in progress by file extensions, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)

    def file_finder(folderpath,file_extensions):
        files=[]
        for file in os.listdir(folderpath):
            for extension in file_extensions:
                if file.endswith(extension):
                    files.append(file)
        return files 

    for extensions_type,extension_tuple in file_extensions.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)

    for extensions_type,extension_tuple in new_path.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
    print("File organizing completed by Extenstions.")


# To Organize the file by size

if typeofsort=="2":
    print("File Organizing in progress by size of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)

    def sizecheck(folderpath):
        list_dir=os.walk(folderpath)
        for dir,filename, file in list_dir:
            for f in file:
                sizeoffile=os.stat(dir+"/"+f).st_size
                try:
                    if sizeoffile < 1024:
                        if os.path.exists(folderpath+"/Byte_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/Byte_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                    elif sizeoffile >= 1024 and sizeoffile < 1000*1024:
                        if os.path.exists(folderpath+"/KiloBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/KiloBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                    elif sizeoffile >= 1000*1024 and sizeoffile <= 1000*1024*1024:
                        if os.path.exists(folderpath+"/MegaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/MegaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                    else:
                        if os.path.exists(folderpath+"/GigaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/GigaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                except FileExistsError:
                    continue
        print("File organizing completed by Size.")
    sizecheck(folderpath)

# To Organize the file by Date and Time
if typeofsort=="3":
    print("File Organizing in progress by date of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    
    def date_sort(folderpath):
        list_dir=os.walk(folderpath)
        for dir,filename, file in list_dir:
            for f in file:
                dateoffile=os.stat(dir+"/"+f).st_size
                try:
                    if dateoffile < 1024:
                        if os.path.exists(folderpath+"/Less than 10 days/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Less than 10 days/"+f)
                        else:
                            os.mkdir(folderpath+"/Less than 10 days/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Less than 10 days/"+f)
                    elif dateoffile >= 1024 and dateoffile < 1000*1024:
                        if os.path.exists(folderpath+"/Morethan 10 days to less than 20 days/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Morethan 10 days to less than 20 days/"+f)
                        else:
                            os.mkdir(folderpath+"/Morethan 20 days to less than 30 days/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Morethan 20 days to less than 30 days/"+f)
                    elif dateoffile >= 1000*1024 and dateoffile <= 1000*1024*1024:
                        if os.path.exists(folderpath+"/A month ago/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/A month ago/"+f)
                        else:
                            os.mkdir(folderpath+"/A month ago/")
                            shutil.move(folderpath+"/"+f, folderpath+"/A month ago/"+f)
                    else:
                        if os.path.exists(folderpath+"/More than a month/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/More than a month/"+f)
                        else:
                            os.mkdir(folderpath+"/More than a month/")
                            shutil.move(folderpath+"/"+f, folderpath+"/More than a month/"+f)
                except FileExistsError:
                    continue
        print("File organizing completed by Date.")
    date_sort(folderpath)
