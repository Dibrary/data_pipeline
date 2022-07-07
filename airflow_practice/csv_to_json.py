
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd

def CSVToJSON():
    df =pd.read_csv('/home/paulcrickard/data.csv')
    for i ,r in df.iterrows():
        print(r['name'])
    df.to_json('/home/paulcrickard/fromAirflow.json', orient='records')


default_args = {
    'owner' :'paulcrickard',
    'start_date' :dt.datetime(2022 ,7 ,7),
    'retries' :1,
    'retry_delay' :dt.timedelta(minutes=5),
}

with DAG('MyCSVDAG',
         default_args = default_args,
         schedule_interval=timedelta(minutes=1),
         ) as dag:
    print_starting = BashOperator(task_id='starting', bash_command='echo "I am reading the CSV now....."')

    CSVJson = PythonOperator(task_id='convertCSVtoJSON', python_callable=CSVToJSON)


print_starting >> CSVJson
