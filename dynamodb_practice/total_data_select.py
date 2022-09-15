
import boto3
from config import config_func
access_key, secret_key = config_func()

'''
DynamoDB에 만들어 놓은 테이블의 key는 address와 uuid 2개다.
'''

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id=access_key,aws_secret_access_key=secret_key)

table = dynamodb.Table('amadas_datas') # 테이블 이름 사용.
print(table.scan()) # 해당 테이블의 데이터를 다 볼 수 있다. 관련 정보도 확인 가능.

datas = table.scan()['Items'] # Items로된 키 안에 데이터들이 있다.

for data in datas:
    print(data['address']) # address만 보기

print("============")

for data in datas:
    print(data['tag']) # tag만 보기


