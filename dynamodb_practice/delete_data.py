
import boto3
from config import config_func
access_key, secret_key = config_func()

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas')
table.delete_item(
    Key={
        'address':'40001',
        'uuid':'aa'
    }
)
print("data delete success")


