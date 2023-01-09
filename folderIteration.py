import os

def folder_iteration(rootdir = "../sub roof data 1"):
    """
    Takes a input folder with many folders in it, and gives back the adress of every file in the subfolders sorted by folder. 
    :param folder: string
    :return: 2d list of strings. 
    """

    roofs = []
    for subdir, dirs, files in os.walk(rootdir):
        for dir in dirs:
            for subdir2, dirs2, files2 in os.walk(os.path.join(subdir, dir)):
                temp = []
                for file in files2:
                    temp.append(os.path.join(subdir, dir, file))
                roofs.append(temp)

    return roofs