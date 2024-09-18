import json
import os

# Classe Base CRUD
class BaseCRUD:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.dados = {}
        self.carregar_dados()

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.dados, f, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                try:
                    self.dados = json.load(f)
                except json.JSONDecodeError:
                    print("Erro no formato do arquivo JSON. Inicializando como vazio.")
                    self.dados = {}
        else:
            self.dados = {}

    def create(self, chave, valor):
        if chave in self.dados:
            print(f"O registro com a chave {chave} já existe.")
        else:
            self.dados[chave] = valor
            self.salvar_dados()
            print(f"Registro {chave} criado com sucesso.")

    def read(self):
        if not self.dados:
            print("Nenhum registro encontrado.")
        else:
            for chave, valor in self.dados.items():
                print(f"{chave}: {valor}")

    def update(self, chave, novos_dados):
        if chave in self.dados:
            self.dados[chave].update(novos_dados)
            self.salvar_dados()
            print(f"Registro {chave} atualizado com sucesso.")
        else:
            print(f"Registro com a chave {chave} não encontrado.")

    def delete(self, chave):
        if chave in self.dados:
            del self.dados[chave]
            self.salvar_dados()
            print(f"Registro {chave} excluído com sucesso.")
        else:
            print(f"Registro com a chave {chave} não encontrado.")


# Classe para CRUD de Clientes, herdando de BaseCRUD
class ClienteCRUD(BaseCRUD):
    def __init__(self, arquivo="clientes.json"):
        super().__init__(arquivo)

    # Método para cadastrar cliente com validação de dados
    def cadastrar_cliente(self, cpf, nome, idade, email):
        cliente = {"Nome": nome, "Idade": idade, "Email": email}
        self.create(cpf, cliente)


# Sistema
class Sistema:
    def __init__(self):
        self.cliente_crud = ClienteCRUD()

    def menu(self):
        while True:
            print("\n1. Cadastrar Cliente")
            print("2. Exibir Clientes")
            print("3. Atualizar Cliente")
            print("4. Excluir Cliente")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cpf = input("Digite o CPF: ")
                nome = input("Digite o Nome: ")
                idade = input("Digite a Idade: ")
                email = input("Digite o E-mail: ")
                self.cliente_crud.cadastrar_cliente(cpf, nome, idade, email)
            elif opcao == "2":
                self.cliente_crud.read()
            elif opcao == "3":
                cpf = input("Digite o CPF do cliente a ser atualizado: ")
                nome = input("Digite o novo nome: ")
                idade = input("Digite a nova idade: ")
                email = input("Digite o novo e-mail: ")
                self.cliente_crud.update(cpf, {"Nome": nome, "Idade": idade, "Email": email})
            elif opcao == "4":
                cpf = input("Digite o CPF do cliente a ser excluído: ")
                self.cliente_crud.delete(cpf)
            elif opcao == "5":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")


# Executa o sistema
sistema = Sistema()
sistema.menu()
