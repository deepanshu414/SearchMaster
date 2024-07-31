import os
import psutil
def main(user):
    def find_file_path(file_name):  
        a=0
        def get_drive_names():
            drives = []
            for partition in psutil.disk_partitions():
                drives.append(partition.device)
            return drives
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

    file_name = str(user)
    if file_name:
        find_file_path(file_name)



