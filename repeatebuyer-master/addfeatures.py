import pandas as pd
from getPath import *
import numpy as np
pardir = getparentdir()
# user_log_path = pardir+'/data/user_log_format1.csv'
user_log_path = pardir+'/testaddfeature.csv'

def get_user_month_features(data):
    usermonthpath = pardir+'/middledata/usermonthfeature.csv'
    months = pd.DataFrame(data['time_stamp'])
    data['month'] = months.applymap(lambda x: (str(x))[:-2])
    c = pd.DataFrame({'count':data.groupby(["user_id","month","action_type"]).size()}).reset_index()

    table = pd.pivot_table(c,values='count',  # 相比values = ['count']，虽然内容一样，但是df还是有区别的：
                                              # 列索引少了一个level ‘count’
                            index = ["user_id","month"],
                            columns = ['action_type'],
                            fill_value=0,
                            aggfunc='mean' # 默认就是mean
                            )

    table = pd.pivot_table(table,values=[0,1,2], # values指的是前面已经生成的table的action_type的取值
                            index = ["user_id"],columns = ['month'],fill_value=0)

    # 这里是二合一的方法：
    # table = pd.pivot_table(data = c,
    #                        values = 'count',
    #                        index = ['user_id'],
    #                        columns = ['aciton_type','month'],
    #                        fill_value = 0
    #                         ).pop([0,1,2])

    table.reset_index(level=["user_id"],inplace = True)

    values = np.array(table.values)
    res = pd.DataFrame()
    res['user_id'] = values[:,0]
    for i in range(1,len(values[0])):
        res[str(i)] = values[:,i] # 难道这不是做了一个重命名的事情？这是什么逻辑？

    res.to_csv(usermonthpath,encoding='utf-8',mode = 'w', index = False)

data = pd.read_csv(user_log_path)
get_user_month_features(data)

