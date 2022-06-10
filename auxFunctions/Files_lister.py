import os, re

def Files_lister(path='.', regex=r'', subfolders=False, filesamount=True):
    
    if re.search(regex, path):
        return [path]

    if subfolders == False:
        files_to_open = [f'{path}/{file}' for file in os.listdir(path) if re.search(regex, file)]

    elif subfolders == True:
        files_to_open=[]
        for file_path, subdirs, files in os.walk(path):
            for file in files:
                path_name = os.path.join(file_path, file)
                if re.search(regex, path_name):
                 files_to_open.append(path_name)
    else:
        raise ValueError('Invalid subfolders argument. Expected True or False')

    if not files_to_open:
        raise Exception('Found 0 files')

    if filesamount==True:
        print(f'Found {len(files_to_open)} files with the specified parameters')
    elif filesamount != False:
        raise ValueError('Invalid filesamount argument. Expected True or False')
    
    return files_to_open

