import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd


# def cleanScooter():
#     df = pd.read_csv('scooter.csv')
#     df.drop(columns=['region_id'], inplace=True)
#     df.columns = [x.lower() for x in df.columns]
#     df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
#     df.to_csv('cleanscooter.csv')
#
#
# def filterData():
#     df = pd.read_csv('cleanscooter.csv')
#     fromd = '2019-05-23'
#     tod = '2019-06-03'
#     tofrom = df[(df['started_at'] > fromd) & (df['started_at'] < tod)]
#     tofrom.to_csv('may23-june3.csv')

def cleanScooter():
    df=pd.read_csv('/root/airflow/dags/scooter.csv') # 이렇게 바꿔주고 나서야 됨;;
    df.drop(columns=['region_id'], inplace=True)
    df.columns=[x.lower() for x in df.columns]
    df['started_at']=pd.to_datetime(df['started_at'],format='%m/%d/%Y %H:%M')
    df.to_csv('/root/airflow/dags/cleanscooter.csv')


def filterData():
    df=pd.read_csv('/root/airflow/dags/cleanscooter.csv') # 이렇게 바꿔주고 나서야 됨;;
    fromd = '2019-05-23'
    tod='2019-06-03'
    tofrom = df[(df['started_at']>fromd)&(df['started_at']<tod)]
    tofrom.to_csv('/root/airflow/dags/may23-june3.csv')


default_args = {
    'owner': 'paulcrickard',
    'start_date': dt.datetime(2020, 4, 13),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG('CleanData',
         default_args=default_args,
         schedule_interval=timedelta(minutes=1),  # '0 * * * *',
         ) as dag:
    cleanData = PythonOperator(task_id='clean',
                               python_callable=cleanScooter)

    selectData = PythonOperator(task_id='filter',
                                python_callable=filterData)

    moveFile = BashOperator(task_id='move',
                            bash_command='echo START')

cleanData >> selectData >> moveFile

# 위 코드로 하면 진행이 안되고 계속 fail남.
# 폴더 경로를 linux에서 인식 못함 =_=;;




