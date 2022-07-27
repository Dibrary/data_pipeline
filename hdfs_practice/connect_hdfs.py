
'''
hadoop version 2.7.2
'''


import pandas as pd
from hdfs import InsecureClient
import os

print("start")
client_hdfs = InsecureClient("http://192.168.56.114:50070")

print(client_hdfs) # <InsecureClient(url='http://192.168.56.114:50070')> 이렇게 결과 나옴.

path = "2022-07-27-data-log"
dt = pd.read_csv(path, encoding="utf-8")
print(dt.head())

with client_hdfs.write("/python/"+path, encoding="utf-8", overwrite=True) as writer:
    dt.to_csv(writer, index=False, header=False, encoding=encType)

print("end")

# with open("../datas/2022-07-25-log") as f:
#     print(f.read())
'''
위 방법은 계속 데이터 가져올 때 에러남.
'''
