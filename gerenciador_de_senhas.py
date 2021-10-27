import sqlite3

senha = "123456789"
senha1 = input("Insira sua senha: ")

if senha1 != senha:
    print("Senha inválida!")
    exit()

connec = sqlite3.connect("senhas.db")

cursor = connec.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    servicos TEXT NOT NULL,
    usuario TEXT NOT NULL,
    senhas TEXT NOT NULL
);
''')

def senhas_salvas(servicos):
    cursor.execute(f'''
    SELECT usuario, senhas FROM users
    WHERE servicos = "{servicos}"
    ''')
    
    if cursor.rowcount == 0:
        print("Serviço não cadastrado. Use listar para verificar os serviços.")
    
    else:
        for user in cursor.fetchall():
            print(user)


def insert_senhas(servicos, usuario, senhas):
    cursor.execute(f'''
    INSERT INTO users (servicos, usuario, senhas)
    VALUES ("{servicos}", "{usuario}", "{senhas}")
    ''')
    connec.commit()


def services_1():
    cursor.execute('''
        SELECT servicos FROM users;
    ''')
    
    for servicos in cursor.fetchall():
        print(servicos)


def menu():
    print("-"*50)
    print("Digite 'inserir' para inserir nova senha:")
    print("Digite 'listar' para listar serviços salvo:")
    print("Digite 'recuperar' para recuperar uma senha:")
    print("Digite 'sair' para sair:")
    print("-"*50)

while True:
    menu()
    opcao = input("O que deseja fazer? ")
    
    if opcao not in ["sair","inserir","listar","recuperar"]:
        print("Opção inválida!")
        continue
    
    elif opcao == "sair":
        break
    
    if opcao == "listar":
        services_1()
    
    if opcao == "recuperar":
        servicos = input("Qual o serviço deseja para buscar a senha? ")
        senhas_salvas(servicos)
    
    if opcao == "inserir":
        servicos = input("Qual o serviço? ")
        usuario = input("Qual o usuario? ")
        senhas = input("Qual a senha? ")
        insert_senhas(servicos, usuario, senhas)

connec.close()
