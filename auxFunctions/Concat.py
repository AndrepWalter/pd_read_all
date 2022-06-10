import pandas

def Concat(dataframes, concat=False):
    
    if concat == True:
        dataframes = pandas.concat(dataframes)
    elif concat != False: 
        raise ValueError("Invalid concat argument. Expected True or False")
    
    return dataframes