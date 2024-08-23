import os
import psutil
def searchp(Searching):
    def find_file_path(file_name):  
        a=0
        def get_drive_names():
            try:
                drives = []
                for partition in psutil.disk_partitions():
                    drives.append(partition.device)
                return drives
            except Exception as e:
                print("Error: "+str(e))
        drive_names = get_drive_names()
        for drive in drive_names:
            for root, dirs, files in os.walk(drive):
                for file in files:
                    if file and file_name in file: 
                        file_path = os.path.join(root, file)
                        print(file_path)
                        a+=1
        if(a==0):
            print(f"No files found with the name '{file_name}' in any drive.")
        else:
            print(f"Total number of files : {a}")
    try:
        find_file_path(str(Searching))
    except Exception as e:
        print("Error: "+str(e))
def searchl(Searching):
    def find_file_path(file_name):  
        a=0
        def get_drive_names():
            try:
                drives = []
                for partition in psutil.disk_partitions():
                    drives.append(partition.device)
                return drives
            except Exception as e:
                return "Error: "+str(e)
        drive_names = get_drive_names()
        try:
            for drive in drive_names:
                for root, dirs, files in os.walk(drive):
                    for file in files:
                        if file and file_name in file: 
                            file_path = os.path.join(root, file)
                            list_main.append(file_path)
                            a=1
        except Exception as e:
            return "Error: "+ str(e)
        if(a==0):
            list_main.append("None")
    try:
        list_main=[]
        find_file_path(str(Searching))
        return list_main
    except Exception as e:
        return "Error: "+str(e)



