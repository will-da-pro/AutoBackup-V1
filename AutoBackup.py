import shutil
import os
import time
import signal
import sys
import atexit

Path = os.path.realpath(__file__)
sourceDirec, null = os.path.split(Path)
print(sourceDirec)
fileName = raw_input("Please enter the file name: ")
File, Extension = os.path.splitext(fileName)
print(File + ", " + Extension)

def createBackup():
    path, dirs, files = next(os.walk(sourceDirec + '/Backups/'))
    fileCount = len(files)
    BackupNum = str(fileCount + 1)
    
    source = (sourceDirec + "/" + File + Extension)
    destination = (sourceDirec + "/Backups/" + File + BackupNum + Extension)

    backupGUI(fileCount, source, destination)
    
    shutil.copy(source, destination)

def checkBackupsFolder(File):
    if os.path.isdir(File + "/Backups/"):
        return
    else:
        os.makedir(File + "/Backups/")

def backupGUI(fileCount, source, destination):
    print("")
    print("Creating new backup...")
    print("Number of current backups: " + str(fileCount))
    print("Source: " + source)
    print("Destination: " + destination)

def handle_exit():
    createBackup()

atexit.register(handle_exit)
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

while True:
    time.sleep(300)
    createBackup()


