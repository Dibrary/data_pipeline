
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import psycopg2 as db

default_args = {
    'owner': 'paulcrickard',
    'start_date' :dt.datetime(2020, 4, 2),
    'retries' :1,
    'retry_delay' :dt.timedelta(minutes=5),
}

def _queryPostgresql():
    conn_string ="dbname='dataengineering' host=192.168.0.121 user='postgres' password='qlalfqjsgh'"
    conn = db.connect(conn_string)
    df = pd.read_sql("Select name, city from users", conn)
    df.to_csv('postgresqldata.csv')
    print("the finish making data file")

def _printData():
    f = open('postgresqldata.csv')
    f.read()

with DAG('MyDBdag',
         default_args=default_args,
         schedule_interval=timedelta(minutes=5),
         # '0 * * * *',
         ) as dag:
    getData = PythonOperator(task_id='QueryPostgreSQL', python_callable=_queryPostgresql)

    printData = PythonOperator(task_id='PrintData', python_callable=_printData)

getData >> printData


# 실행 결과 postgresqldata.csv 파일이 생성된다.
# 메서드가 DAG의 python_callable 위에 있어야 인식할 수 있다.
# scheduler를 동작시키면 해당 파일에 어떤 에러가 있는지 알 수 있다.
# dags 폴더에 넣어도 scheduler를 실행하지 않으면 파일 인지 못함.
# postgresql에서 IPv4의 허용 IP 중에 0.0.0.0/0이 없으면 vm에서 접속 불가능.

