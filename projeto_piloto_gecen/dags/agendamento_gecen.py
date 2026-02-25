from airflow import DAG  # Linha 1: Importa a "ferramenta de agendamento"
from datetime import datetime  # Linha 2: Importa o "calendário" do Python
from airflow.operators.python import PythonOperator # Linha 3: Ferramenta para rodar seu código Python