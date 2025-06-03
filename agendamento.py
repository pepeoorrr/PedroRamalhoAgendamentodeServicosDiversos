import mysql.connector

# Conexão com o banco de dados MySQL (via XAMPP)
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Deixe em branco se estiver usando XAMPP padrão
    database="agendamentos"
)

cursor = conexao.cursor()

# Criar tabela, se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(255),
    tipo_servico VARCHAR(255),
    data_agendamento DATE,
    endereco TEXT
)
""")
conexao.commit()

# Funções de operação
def inserir_agendamento(nome, tipo, data, endereco=None):
    sql = "INSERT INTO agendamentos (nome_cliente, tipo_servico, data_agendamento, endereco) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, tipo, data, endereco))
    conexao.commit()

def listar_agendamentos():
    cursor.execute("SELECT * FROM agendamentos")
    resultados = cursor.fetchall()
    for ag in resultados:
        print(f"ID: {ag[0]} | Cliente: {ag[1]} | Serviço: {ag[2]} | Data: {ag[3]} | Endereço: {ag[4]}")
    return resultados

def editar_nome_cliente(id_agendamento, novo_nome):
    sql = "UPDATE agendamentos SET nome_cliente = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, id_agendamento))
    conexao.commit()

def remarcar_agendamento(id_agendamento, nova_data):
    sql = "UPDATE agendamentos SET data_agendamento = %s WHERE id = %s"
    cursor.execute(sql, (nova_data, id_agendamento))
    conexao.commit()

def excluir_agendamento(id_agendamento):
    sql = "DELETE FROM agendamentos WHERE id = %s"
    cursor.execute(sql, (id_agendamento,))
    conexao.commit()

# Menu interativo
def menu():
    while True:
        print("\n===== MENU DE AGENDAMENTOS =====")
        print("1. Cadastrar Agendamento")
        print("2. Listar Agendamentos")
        print("3. Editar Nome do Cliente")
        print("4. Remarcar Agendamento")
        print("5. Excluir Agendamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Cliente: ")
            tipo = input("Tipo de Serviço: ")
            data = input("Data do Agendamento (AAAA-MM-DD): ")
            endereco = input("Endereço do Serviço (opcional): ")
            inserir_agendamento(nome, tipo, data, endereco)
            print("✅ Agendamento inserido com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de Agendamentos ---")
            listar_agendamentos()

        elif opcao == "3":
            listar_agendamentos()
            id_edit = input("ID do agendamento: ")
            novo_nome = input("Novo nome do cliente: ")
            editar_nome_cliente(id_edit, novo_nome)
            print("✅ Nome atualizado.")

        elif opcao == "4":
            listar_agendamentos()
            id_remarcar = input("ID do agendamento: ")
            nova_data = input("Nova data (AAAA-MM-DD): ")
            remarcar_agendamento(id_remarcar, nova_data)
            print("✅ Data remarcada.")

        elif opcao == "5":
            listar_agendamentos()
            id_excluir = input("ID do agendamento: ")
            excluir_agendamento(id_excluir)
            print("✅ Agendamento excluído.")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("❌ Opção inválida!")

# Executa o menu
menu()

# Fecha a conexão no final
cursor.close()
conexao.close()
