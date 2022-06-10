import pandas

def Col_rename(dataframes, colnames):
    
    if colnames is None:
        pass
    elif type(colnames) == dict:
        if type(dataframes)==list:
            for dataframe in dataframes:
                if type(dataframe) == pandas.core.frame.dataframe:
                    dataframe.rename(columns=colnames, inplace=True)
                else:
                    raise TypeError('Invalid Dataframe type. Expected pandas dataframe os list of  pandas dataframe')
        elif type(dataframes) == pandas.core.frame.DataFrame:
            dataframes.rename(columns=colnames, inplace=True)
        else:
            raise TypeError('Invalid Dataframe type. Expected pandas dataframe os list of dataframe')
    elif type(colnames) in [list, set]:
        list(colnames)
        colnames = {dataframes.columns[idx]:colname for idx, colname in enumerate(colnames)}
        print(colnames)
        #for idx, colname in colnames:
        dataframes.rename(columns=colnames, inplace=True)
    else:
        raise ValueError("Invalid colname argument. Expected List, dict or None")
    
    return dataframes
