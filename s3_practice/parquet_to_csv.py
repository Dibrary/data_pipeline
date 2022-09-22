
import pandas as pd
df = pd.read_parquet('data.parquet')
print(df)

df.to_csv("event_data.csv")



