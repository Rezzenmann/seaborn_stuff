def annotate_each_n_value(data:pd.DataFrame, each_n:int=5):
    cols = [col for col in data.columns if col not in data.iloc[:,::each_n].columns]
    data[cols] = ''
    return data
