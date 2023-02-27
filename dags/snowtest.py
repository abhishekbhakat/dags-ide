from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2023,2,27), catchup=False, schedule=None)
def debug_conn():

    @task
    def print_conn(conn_id):
        from airflow.models import Connection
        conn = Connection.get_connection_from_secrets(conn_id)
        print(conn.host)
        print(conn.conn_type)
        print(conn.debug_info)
        print(conn.get_uri)
        print(conn.extra)
    
    print_conn('test_snowflake')

dg = debug_conn()