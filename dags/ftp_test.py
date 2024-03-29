"""
ftp_test
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from airflow.providers.amazon.aws.transfers.sftp_to_s3 import SFTPToS3Operator
from astro import sql as aql
import pandas as pd
import pendulum

from airflow.models import Connection

@aql.dataframe(task_id="python_1")
def python_1_func():
    from airflow.models import Connection
    c = Connection.get_connection_from_secrets('ftp_test')
    print(c.__dir__())
    print(c.conn_type)

default_args={
    "owner": "Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2023-07-26", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Open in Cloud IDE": "https://cloud.astronomer.io/cl0n1675p186971fwyfaumecrc/cloud-ide/cleiioon5008i01krj5dqtaku/clkjk6pei000101o5eet5vv6k",
    },
)
def ftp_test():
    python_1 = python_1_func()

    s_f_t_p_to_s3_operator_1 = SFTPToS3Operator(
        task_id="s_f_t_p_to_s3_operator_1",
    )

dag_obj = ftp_test()
