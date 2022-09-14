
'''
S3에 최상위 폴더는 버킷이고 그 뒤에서부터는 /를 붙여가며 Key가 된다.
'''
import io

import pandas as pd
import boto3
from config import config_func # 단순히 설정파일을 사용하기 위해 임의로 만듦.

s3 = boto3.client("s3", aws_access_key_id=config_func()[0],
                        aws_secret_access_key=config_func()[1],
                        region_name="ap-northeast-2")

# obj_list = s3.get_object(Bucket="amadaslogbucket", Key="logs/MODBUS.csv")
# print(obj_list)
'''
'Body': <botocore.response.StreamingBody object at 0x000001C6F51CE948> # Body는 이런 형태로 나온다.
'''

# df = pd.read_csv(io.BytesIO(obj_list["Body"].read()))
# print(df)
# 여기서 pandas.errors.ParserError: Error tokenizing data. C error: Expected 4 fields in line 24, saw 5 에러 난다. 왜? 콤마로 자를 때 갯수가 행(row)마다 달라서


obj_list = s3.get_object(Bucket="amadaslogbucket", Key="logs/status_data.csv")
print(obj_list)

df = pd.read_csv(io.BytesIO(obj_list["Body"].read())) # 모든 행(row)가 column갯수가 같아야 한다.
print(df)


