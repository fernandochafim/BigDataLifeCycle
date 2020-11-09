"""
Fernando Chafim

"""

from datetime import datetime
from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
#from airflow.operators.python_operator import PythonOperator
#from airflow.operators.hive_operator import HiveOperator

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "airflow"
}

first_file = 'youtubetrending_' + datetime.now().strftime("%Y%m%d") + '.json'

with DAG(dag_id="youtube_dag", schedule_interval="@daily", default_args=default_args) as dag:
    #  Space after the bash script name because Airflow apply a Jinja template to it,
    scraping_youtube = BashOperator(task_id="scraping_youtube", bash_command="/mnt/d/BigDataLifeCycle/dags/dataprocessing/start_scraping.sh ")
    
    waiting_for_scraped_data = FileSensor(task_id="waiting_for_scraped_data", fs_conn_id="fs_youtube", filepath=first_file, poke_interval=5)

    generating_datasets = BashOperator(task_id="scraping_youtube", bash_command="/mnt/d/BigDataLifeCycle/dags/dataprocessing/generating_datasets.sh ")

    #TODO
    #storing_tabular_datalake = BashOperator(task_id="storing_tabular_datalake", bash_command="hadoop fs -put -f /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_{{ execution_date }}.csv /tmp/")

    #storing_images_datalake = BashOperator(task_id="storing_images_datalake", bash_command="hadoop fs -put -f /mnt/d/BigDataLifeCycle/TrendingAnalytics/output/images/{{ execution_date }}/* /tmp/images")

    #loading_into_database = HiveOperator(task_id="loading_youtube", hql="LOAD DATA INPATH '/mnt/d/BigDataLifeCycle/TrendingAnalytics/output/csv/youtubetrending_tabular_{{ execution_date }}.csv' INTO TABLE youtube")