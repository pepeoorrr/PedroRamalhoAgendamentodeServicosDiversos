import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Deixe vazio se você não colocou senha no MySQL
        database="agendamentos"
    )

    if conexao.is_connected():
        print("✅ Conexão com o banco de dados 'agendamentos' estabelecida com sucesso!")
        conexao.close()

except mysql.connector.Error as erro:
    print(f"❌ Erro ao conectar ao MySQL: {erro}")
