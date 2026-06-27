#E-commerce DAG 
#IMPORT Libraries
from datetime import timedelta, datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator


#Dag arguments
default_args= {
    'owner': 'Abdallah',
    'email': 'Abdallah.MohsenAhmed94@gmail.com',
    'start_date': datetime(2026,6,27),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}
#Dag definition
dag = DAG(
    'E-commerce_analytics',
    description = 'E-commerce analytics',
    default_args = default_args,
    schedule = timedelta(days=1),
)

#Task definition
start_pipeline = BashOperator(
    task_id = 'Starting_the_pipeline',
    bash_command = 'echo "Starting the pipeline..."',
    dag = dag,
)

generate_raw_data = BashOperator(
    task_id= 'generate_orders_transactions',
    bash_command = 'python3 /opt/airflow/dags/generate_raw_data.py',
    dag = dag,
)

transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = 'python3 /opt/airflow/dags/transform_data.py',
    dag = dag,
)

end_pipeline = BashOperator(
    task_id = 'end_pipeline',
    bash_command = 'echo "Pipeline completed successfully!"',
    dag = dag,
)

#Task pipeline
start_pipeline >> generate_raw_data >> transform_data >> end_pipeline