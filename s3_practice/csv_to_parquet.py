
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import datetime as dt

csv_file = "attribution_part-00000"

parquet_file = "attribution_data.parquet"
chunksize = 300000

def reschema(chunk):
    header = ['partner','campaign','server_datetime','tracker_id','log_id','attribution_type','identity_adid']
    chunk.columns = header
    chunk['partner'] = chunk['partner'].replace(np.nan, '0')
    chunk['campaign'] = chunk['campaign'].replace(np.nan, '0')
    chunk['tracker_id'] = chunk['tracker_id'].replace(np.nan, '0')
    chunk['attribution_type'] = chunk['attribution_type'].astype(int)
    chunk['server_datetime'] = pd.to_datetime(chunk['server_datetime'], errors = 'coerce')
    chunk['server_datetime'] = chunk['server_datetime'].apply(lambda x: pd.Timestamp('1990-01-01 01:01:01') if type(x) == type(pd.NaT) else x)
    # 0001-01-01 00:00:00 에 대한 처리를 전체 데이터 구간에 포함되지 않는 1990-01-01 01:01:01이라는 임의의 값으로 통일함

    return chunk

csv_stream = pd.read_csv(csv_file, sep=',', chunksize=chunksize, low_memory=False, dtype=str,
                         header=None)  # low_memory=False는 파일 정보 누락 없이 가져온다.

for i, chunk in enumerate(csv_stream):
    chunk = reschema(chunk)
    print("Chunk", i)

    parquet_schema = pa.Table.from_pandas(df=chunk).schema
    if i == 0:
        parquet_writer = pq.ParquetWriter(parquet_file, parquet_schema, compression='snappy')
    table = pa.Table.from_pandas(chunk, schema=parquet_schema)
    parquet_writer.write_table(table)

parquet_writer.close()


