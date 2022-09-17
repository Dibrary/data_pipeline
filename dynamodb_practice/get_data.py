

import boto3
from config import config_func

access_key, secret_key = config_func()

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas')

data = table.get_item(
    Key = {
        'address':'40001',
        'uuid':'aa'
    }
)

print(data)
'''
해당되는 key의 데이터가 없으면 이 결과가 나옴. 
{'ResponseMetadata': {'RequestId': 'KAC009J50O94SPVBBQ8PNCMUO3VV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 
'HTTPHeaders': {'server': 'Server', 'date': 'Wed, 14 Sep 2022 23:32:09 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '2', 
'connection': 'keep-alive', 'x-amzn-requestid': 'KAC009J50O94SPVBBQ8PNCMUO3VV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}
'''

real_data = data['Item'] # dict 꼴로 받아오는데 실제 key-value는 Item 안에 있다.

for x in real_data.keys():
    print(real_data[x])

