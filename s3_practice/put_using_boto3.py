
# from get_using_boto3 import s3
import boto3
from config import config_func # 단순히 설정파일을 사용하기 위해 임의로 만듦.

access_key, secret_key = config_func()
s3 = boto3.client("s3", aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        region_name="ap-northeast-2")

s3.upload_file("udata.csv", 'amadaslogbucket', 'logs/status_data.csv')
# 순서대로 '로컬에서 올릴 파일 이름', '버킷 이름', '버킷에 저장될 파일 이름' 이다.

print("업로드 완료")
# 정상적으로 업로드 됨 확인.

