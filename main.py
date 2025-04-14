import pandas as pd
from connection import create_connection

#A JUNÇÃO DO DB COM EXCEL PARA INSERIR NO DATABASE

#CONEXÃO
conn = create_connection()
cursor = conn.cursor()

#LEITURA E TRATAMENTO DO EXCEL
df = pd.read_excel("dados_tratados.xlsx")
df = df.where(pd.notna(df), None)

#UMA QUERY PARA INSERIR OS DADOS NO DATABASE
query = """
    INSERT INTO access_logs (nome_usuario, email, ip, data_hora_login, status_login, navegador, sistema_operacional)
    VALUES (%s, %s, %s, %s, %s, %s, %s)

"""

#PERCORRE TDO O EXCEL INSERINDO OS DADOS POR LINHAS
for _, row in df.iterrows():
    valores= tuple(row)
    cursor.execute(query, valores)

#EXECUTA E FECHA O DB
conn.commit()
cursor.close()

print("Dados inseridos no DB com sucesso!")
