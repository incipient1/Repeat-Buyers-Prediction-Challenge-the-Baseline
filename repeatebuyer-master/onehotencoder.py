# 这个文件在其它文件中被导入了，不能删

import pandas as pd
import numpy as np
from getPath import *
from sklearn.preprocessing import OneHotEncoder

pardir = getparentdir()

def encoder(arr):
    ohe = OneHotEncoder(sparse=False) # categorical_features='all',
    ohe.fit(arr)
    return ohe.transform(arr)

def encodebins(bins):
    arr = [[a] for a in range(bins)]
    res = encoder(arr)
    return res

if __name__=="__main__":
    arr = encodebins(9)
    a = arr[0]
    print(len(a))
    print(a[1])