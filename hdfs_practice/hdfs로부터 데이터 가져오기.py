
import pandas as pd
from hdfs import InsecureClient
import os

print("start")
client_hdfs = InsecureClient("http://192.168.56.114:50070", user='root')

client_hdfs.delete("/test") # 폴더 삭제는 된다.
print("폴더 삭제")

client_hdfs.write("/webhdfs/test.txt", "test string") # linux에서 코딩한 경우는 들어간다.
print("데이터 한줄 추가.")

with client_hdfs.read("/webhdfs/v1/flume/temp.1658890201591.log", encoding='utf-8') as reader:
    print(reader.read()) # linux에서 코딩한 경우는 읽어온다.

    # data = pd.read_csv(reader, engine='python', encoding='utf-8', on_bad_lines='skip')
    # print(data.head())

print("stop")

# 파이썬에서 read할 때 경로는 /webhdfs/v1 이다.
# /flume 이렇게 설정하면 /webhdfs/v1/flume 이렇게 찾아 들어간다고 생각함.

'''
socket.gaierror: [Errno 11001] getaddrinfo failed

requests.exceptions.ConnectionError: HTTPConnectionPool(host='slave2.hadoop.com', port=50075): 
Max retries exceeded with url: /webhdfs/v1/flume/temp.1658890201591.log?op=OPEN&user.name=kkdh8&namenoderpcaddress=master.hadoop.com:9000&offset=0 
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000029C79859E88>: 
Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
위 에러가 계속 나면서 안 됨.

requests.exceptions.ConnectionError: HTTPConnectionPool(host='slave1.hadoop.com', port=50075): Max retries exceeded with url:
 /webhdfs/v1/user/root/temp.1658890201591.log?op=OPEN&user.name=root&namenoderpcaddress=master.hadoop.com:9000&offset=0 
 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000002368B9C8F08>: 
Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

에러가 이렇게 바뀌어서 /user/root 안에 파일을 넣어봤는데 안 된다.

requests.exceptions.ConnectionError: HTTPConnectionPool(host='slave1.hadoop.com', port=50075): 
Max retries exceeded with url: /webhdfs/v1/webhdfs/test.txt?op=CREATE&user.name=root&namenoderpcaddress=192.168.56.114:9000&overwrite=false&user.name=root 
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001D1F0B594C8>: 
Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
namenode 의 core-site.xml에서 master.hadoop.com 쓰는 부분을 일일이 192.168.56.114로 수정해도 안 됨.

'''

