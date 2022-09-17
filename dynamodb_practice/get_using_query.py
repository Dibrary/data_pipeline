
import boto3
from boto3.dynamodb.conditions import Key, Attr # 쿼리 쓰려면 Key, Attr 불러와야함.
from config import config_func
access_key, secret_key = config_func()

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas')
result = table.query(
    KeyConditionExpression=Key('address').eq('40002')
)

print(result['Items'])

# results = table.query(
#     KeyConditionExpression=Key('name').eq('validation_tag') # 이렇게는 안 된다. name은 Key가 아니므로.
# )


