import sqlite3
import pandas as pd

def get_connection(db_path="db/database.db"):
    """
    Retorna uma conexão com o banco SQLite.
    """
    conn = sqlite3.connect(db_path)
    return conn

def get_cities():
    """
    Retorna uma lista com todas as cidades distintas do banco.
    """
    conn = get_connection()
    query = "SELECT DISTINCT city FROM houses ORDER BY city;"  # ajuste o nome da tabela
    cities_df = pd.read_sql_query(query, conn)
    conn.close()
    return cities_df["city"].tolist()