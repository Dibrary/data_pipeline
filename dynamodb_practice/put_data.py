
import boto3
from config import config_func

access_key, secret_key = config_func()

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas')
table.put_item(
    Item = {
        'address':'40011',
        'tag':'01-AT007-VV1',
        'name':'validation_tag',
        'uuid':'abe' # 임의로 넣어봄.
    }
)
print("put success")
