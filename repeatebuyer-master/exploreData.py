import pandas as pd
from getPath import *
pardir = getparentdir()

def analyze_train():
    data = pd.read_csv(pardir+'/data/user_log_format1.csv')
    countdf = pd.DataFrame({'count':data.groupby("item_id")['merchant_id'].nunique()}).reset_index()
    # 求出每一个item_id有多少个merchant_id在卖它

    morethanone = countdf['item_id'][countdf['count']>1]
    # 找到非专卖的商品，以及卖它的merchant_id的数量

    print(morethanone)
    # users = len(data.groupby('user_id').size())
    # merchants = len(data.groupby('merchant_id').size())
    # positives = data['label'][data['label']==1]
    # data.rename(index=str, columns={'seller_id':'merchant_id'}, inplace=True)
    # data.to_csv(pardir+'/data/user_log_format1.csv',encoding='utf-8',mode = 'w', index = False)
    # del data
    # print(data)
    # print(users)
    # print(merchants)
    # print(len(positives))
    # print(len(data))
    # print(len(positives)/len(data))

def analyze_train_label():
    data = pd.read_csv(pardir+'/rawdata/data_format2/train_format2.csv')
    print(len(data))
    print(len(data[data['label']==-1]))

def analyze_train_data():
    data = pd.read_csv(pardir+'/middledata/train_split1.csv') # train_split1这个文件是从哪里来的呢？
    countdf = pd.DataFrame({'count':data.groupby(["merchant_id","user_id"])['label'].nunique()}).reset_index()

    morethanone = countdf[["merchant_id","user_id"]][countdf['count']>1]
    # 这里是想找到对merchant_id来说处于摇摆区的user_id：因为label的种类多于1，说明这个user_id对merchant_id来说既是忠诚用户、又不是；
    # 怎么理解？
    print(morethanone)

analyze_train_data()




