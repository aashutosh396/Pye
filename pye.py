import os
from sys import platform

'''
Function that creates folder in a specified place with a specified name.j
---
Parameter Path: Takes the path where the folder has to be created.
Parameter Name: Takes the name of the folder to be created.
'''
def createFolderMac(path,name):

    if platform == "linux" or platform == "linux2":
        # linux
        pass
    elif platform == "darwin":

        if path == "":
            print("current path")
        elif path[-1] != "/":
            os.system("mkdir " + path + "/" + name)
            print("Without back slash")
        elif path[-1] == "/":
            os.system("mkdir " + path + name)
            print("With back slash")
            
        print("Folder name", name)
    elif platform == "win32":
        # Windows...
        pass
    

if __name__ == "__main__":
    # find the command to get the root directory of MAC

    root = "/Users/apple/"
    Desktop = root + "Desktop/Japis/"
    
    createFolderMac("","")
    print(platform)

