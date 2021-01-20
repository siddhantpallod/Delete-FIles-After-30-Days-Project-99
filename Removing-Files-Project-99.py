import os
import time
import shutil

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete this " + path)

def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print('Unable ro delete the ' + path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime

    return ctime

def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0

    path = 'PATH_TO_DELETE_THE_FOLDER'

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if(os.path.exists(path)):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= getFileOrFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFoldersCount += 1

                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)

                    if seconds >= getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount += 1
                
                for file in files:
                    filePath = os.path.join(rootFolder, file)

                    if(seconds >= getFileOrFolderAge(filePath)):
                        removeFile(filePath)
                        deletedFilesCount += 1
        else:
            if seconds >= getFileOrFolderAge(path):
                removeFile(path)
                deletedFilesCount += 1

    else:
        print(f'"{path}" is not found')
        deletedFilesCount += 1

    print(f'Total folders deleted: {deletedFoldersCount}')
    print(f"Total files deleted:  {deletedFilesCount}")



if __name__ == '__main__':
    main()