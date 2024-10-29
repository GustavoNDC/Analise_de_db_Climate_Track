# db_connection.py
from sqlalchemy import create_engine

def get_connection():
        host='192.168.0.4'  # IP do seu notebook
        port=5433
        database='mydatabase'
        user='myuser'
        password='secret'

        # Cria a URI para o SQLAlchemy
        uri = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
        engine = create_engine(uri)

        return engine.connect()  # Retorna a conexão do SQLAlchemy
