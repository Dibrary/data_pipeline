
import pandas as pd

path = "2022-07-27-data-log"
dt = pd.read_csv(path, encoding="cp949")

print(dt.describe()) # value에 대한 기본적인 통계치

print(type(dt))
print(dt.describe()) # value에 대한 기본적인 통계치

print(dt.columns) # 컬럼 확인