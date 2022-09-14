
'''
boto3는 AWS용 SDK다.

boto3를 쓸 때 '자격증명'과 '비자격증명' 2가지 데이터 유형이 있다.
'''

import boto3
from config import config_func # 단순히 설정파일을 사용하기 위해 임의로 만듦.

access_key, secret_key = config_func()

s3 = boto3.client("s3", aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name="ap-northeast-2")
obj_list = s3.list_objects(Bucket="amadaslogbucket", Prefix="logs/")

contents_list = obj_list["Contents"]
for x in contents_list:
    print(x)

# 정상으로 읽어오기 성공!




