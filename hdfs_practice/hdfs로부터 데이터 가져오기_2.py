
from pywebhdfs.webhdfs import PyWebHdfsClient


HDFS_CONNECTION = PyWebHdfsClient(host='192.168.56.114',port='50070', user_name='root')

tmp = HDFS_CONNECTION.list_dir('/webhdfs/v1/flume')
print(tmp)
'''
{'FileStatuses': {'FileStatus': [{'accessTime': 1658898804409, 'blockSize': 134217728, 
'childrenNum': 0, 'fileId': 20481, 'group': 'supergroup', 'length': 440, 'modificationTime': 1658898806168, 'owner': 'root',
 'pathSuffix': 'temp.1658890201591.log', 'permission': '644', 'replication': 2, 'storagePolicy': 0, 'type': 'FILE'}]}}
 
위 결과가 나옴. (해당 경로에 파일은 temp.1658890201591.log 이거 하나만 넣어놨었음)

위 코드 사용하기 전에

hdfs-site.xml 파일에서
<property>
<name>dfs.webhdfs.enabled</name>
<value>true</value>
</property>
설정 추가함

'''

my_data = '01010101010101010101010101010101'
my_file = '/user/root/temp.1658890201591.log'
HDFS_CONNECTION.append_file(my_file, my_data) # 여기서도 추가하려면 똑같은 에러가 난다.
print("파일 추가 완료")
# 리눅스에서 쓰려고 할 떄 Permission denied 권한 문제가 있는듯 하다.
