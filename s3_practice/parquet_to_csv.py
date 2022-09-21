
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import decimal as D

csv_file = "event_part-00000"
parquet_file = "event_data.parquet"
chunksize = 500000

def reschema(chunk):
    header = ['identity_adid','os','model','country','event_name','log_id','server_datetime','quantity','price']
    chunk.columns = header
    chunk['server_datetime'] = pd.to_datetime(chunk['server_datetime'], errors='coerce')
    chunk['server_datetime'] = chunk['server_datetime'].apply(lambda x: pd.Timestamp('1990-01-01 01:01:01') if type(x) == type(pd.NaT) else x)
    chunk['quantity'] = chunk['quantity'].replace(np.nan, 0)
    chunk['quantity'] = chunk['quantity'].astype(int)
    chunk['price'] = chunk['price'].replace(np.nan, 0)
    chunk['price'] = chunk['price'].apply(lambda x: D.Decimal(x))

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


