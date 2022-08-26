import webbrowser, os
from pathlib import Path

def Openfolder(path):
    webbrowser.open(path)
    pass

def OpenMultipleSubfolders():
    Items = input(str('Enter main directory:' ))
    Sub = input(str('Enter subfolder:' ))
    parent = Path(Items).parent
    items = parent.iterdir()
    lists = [item.as_posix() for item in items]
    for list in lists:
        webbrowser.open(list + Sub)

def MakeMultipleFolders(Path):
    for i in range(1, 11):
        os.mkdir(Path + f'\\Folder {i}')

def MakeMultipleSubfolders(Items):
    parent = Path(Items).parent
    items = parent.iterdir()
    lists = [item.as_posix() for item in items]
    for list in lists:
        os.mkdir(list + '\\Test')

