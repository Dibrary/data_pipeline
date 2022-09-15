
import boto3
from boto3.dynamodb.conditions import Key, Attr # 쿼리 쓰려면 Key, Attr 불러와야함.
from config import config_func
access_key, secret_key = config_func()

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas')

result = table.scan(
    # FilterExpression=Attr('uuid').lt(27)
    FilterExpression=Attr('uuid').eq('aa')
)

for data in result['Items']:
    print(data)
print("================================================================================")
results = table.scan(
    FilterExpression=Attr('name').eq('validation_tag')
)

for data in results['Items']:
    print(data)



