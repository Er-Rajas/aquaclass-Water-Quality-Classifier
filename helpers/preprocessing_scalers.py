import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler

def Standard_Scale(Train,Test=None):
    scaler = StandardScaler()
    if Test is None :
        scaler_trian = scaler.fit_transform(Train)
        return scaler_trian
    else :
        scaler_trian = scaler.fit_transform(Train)
        scaler_test = scaler.transform(Test)
        return scaler_trian,scaler_test
    
def MINMAX_Scale(Train,Test=None):
    scaler = MinMaxScaler()
    if Test is None :
        scaler_train = scaler.fit_transform(Train)
        return scaler_train
    else : 
        scaler_trian = scaler.fit_transform(Train)
        scaler_test = scaler.transform(Test)
        return scaler_trian,scaler_test