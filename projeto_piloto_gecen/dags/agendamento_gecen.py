from airflow import DAG  # Linha 1: Importa a "ferramenta de agendamento"
from datetime import datetime  # Linha 2: Importa o "calendário" do Python
from airflow.operators.python import PythonOperator # Linha 3: Ferramenta para rodar seu código Python

# Linha 4: Definindo o nome do agendamento e o cronograma
dag_gecen = DAG(
    'agendamento_conexao_sas',       # O nome que vai aparecer no painel do Airflow
    start_date=datetime(2026, 2, 25), # Data de início (hoje)
    schedule='@daily'       # Frequência: Roda uma vez por dia (ex: meia-noite)
)

# Definindo a tarefa que o Airflow vai executar
def executar_script_sas():
    # Aqui o Airflow chama a lógica que você já validou no outro arquivo
    print("Iniciando o Pipeline de Automação do SAS...")

# Criando o operador que liga tudo
tarefa_final = PythonOperator(
    task_id='executar_conexao_sas',
    python_callable=executar_script_sas, # Chama a função acima
    dag=dag_gecen
)