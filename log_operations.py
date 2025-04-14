from connection import create_connection

#CRIEI A TABELA NO DB
def insert_column():
    conn = create_connection()
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS access_logs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(255),
            email VARCHAR(255),
            ip VARCHAR(15),
            data_hora_login DATETIME,
            status_login VARCHAR(50),
            navegador VARCHAR(100),
            sistema_operacional VARCHAR(100)
        )
    """)

    conn.commit()
    cursor.close()

    print('Tabela criada com sucesso!')

insert_column()