

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

real_data = data['Item'] # dict 꼴로 받아오는데 실제 key-value는 Item 안에 있다.

for x in real_data.keys():
    print(real_data[x])

