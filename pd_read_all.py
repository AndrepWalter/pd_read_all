import pandas
from auxFunctions.Col_rename import Col_rename
from auxFunctions.Concat import Concat
from auxFunctions.Files_lister import Files_lister

def read_all(path='.',regex=r'.xls',filesamount=True,subfolders=False, concat=False,colnames=None,pandasfunction=pandas.read_excel, **pythonargs):
    print(*pythonargs)
    files_to_open = Files_lister(path=path, regex=regex, subfolders=subfolders, filesamount=filesamount)
    
    dataframes=[pandasfunction(file, **pythonargs) for file in files_to_open]

    dataframes = Concat(dataframes, concat=concat)

    dataframes = Col_rename(dataframes=dataframes, colnames=colnames)

    return dataframes
