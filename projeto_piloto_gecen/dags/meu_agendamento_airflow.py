from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Definição do agendamento
with DAG(
    'teste_conexao_sas',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily', # Roda todo dia à meia-noite
    catchup=False
) as dag:

    # A tarefa: rodar o script que você já criou e validou
    tarefa_sas = BashOperator(
        task_id='executar_python_sas',
        bash_command='python /caminho/para/seu/projeto_piloto_gecen/file_test_connection.py'
    )