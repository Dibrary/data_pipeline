
from get_using_boto3 import s3

s3.upload_file("status_data.csv", 'amadaslogbucket', 'logs/status_data.csv')
# 순서대로 '로컬에서 올릴 파일 이름', '버킷 이름', '버킷에 저장될 파일 이름' 이다.

print("업로드 완료")
# 정상적으로 업로드 됨 확인.

