import json
import os

class Cliente:
    def __init__(self, nome: str, idade: int, email: str) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email

    def mostrar_cliente(self) -> dict:
        return {"Nome": self.nome, "Idade": self.idade, "E-mail": self.email}


class Sistema:
    def __init__(self) -> None:
        self.cadastro = {}
        self.carregar_dados()


    # Função para salvar dados no arquivo cadastros.json
    def salvar_dados(self, arquivo="MODULO_POO/PROJETO_CRUD/cadastros.json"):
        with open(arquivo, "w") as arquivo_json:
            json.dump({cpf: cliente.__dict__ for cpf, cliente in self.cadastro.items()}, arquivo_json, indent=4)

    # Função para carregar dados do arquivo cadastros.json
    def carregar_dados(self, arquivo="MODULO_POO/PROJETO_CRUD/cadastros.json"):
        if os.path.exists(arquivo):  # Verifica se o arquivo existe
            with open(arquivo, "r") as arquivo_json:
                conteudo = arquivo_json.read().strip()
                if conteudo:  # Verifica se o arquivo não está vazio
                    dados = json.loads(conteudo)
                    self.cadastro = {cpf: Cliente(**cliente) for cpf, cliente in dados.items()}
        else:
            print("Arquivo não encontrado. Nenhum dado foi carregado.")


    # Função para criar um novo cliente
    def create(self, cpf: str):
        nome = input("Digite o nome do cliente: ").capitalize().strip()
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o e-mail do cliente: ")
        self.cadastro[cpf] = Cliente(nome, idade, email)
        self.salvar_dados()  # Salva todos os dados no arquivo após criar o cliente
        print(f"Cliente com CPF {cpf} cadastrado com sucesso!")


    # Função para imprimir os clientes cadastrados
    def read(self):
        if not self.cadastro:
            print("Nenhum cliente cadastrado.")
        else:
            for cpf, cliente in self.cadastro.items():
                print(f"CPF: {cpf}")
                info_cliente = cliente.mostrar_cliente()
                for key, value in info_cliente.items():
                    print(f"{key}: {value}")
                print("-" * 20)
    
     # Função para alterar dados de um cliente
    def update(self, cpf: str):
        if cpf in self.cadastro:
            cliente = self.cadastro[cpf]
            print("Deixe em branco se não quiser alterar o campo.")
            nome = input(f"Digite o novo nome do cliente (atual: {cliente.nome}): ")
            if nome:
                cliente.nome = nome

            idade = input(f"Digite a nova idade do cliente (atual: {cliente.idade}): ")
            if idade:
                cliente.idade = int(idade)

            email = input(f"Digite o novo e-mail do cliente (atual: {cliente.email}): ")
            if email:
                cliente.email = email

            self.salvar_dados()  # Salva todos os dados no arquivo após a atualização
            print(f"Cadastro do cliente com CPF {cpf} alterado com sucesso!")
        else:
            print("Cliente não encontrado.")

    # Função para deletar um cliente do cadastro
    def delete(self, cpf: str):
        if cpf in self.cadastro:
            self.cadastro.pop(cpf)
            self.salvar_dados()  # Salva os dados após a exclusão
            print(f"O cliente {cpf} foi deletado do cadastro.")
        else:
            print("Cliente não encontrado.")


    
    # Função para sair do sistema
    def sair(self) -> bool:
        print("Saindo do sistema. Até logo!")
        return True

    # Menu principal
    def menu(self) -> None:
        while True:
            print('-' * 40)
            print("| Escolha uma opção:                   |")
            print("|                                      |")
            print("| 1. Cadastrar novo cliente            |")
            print("| 2. Alterar cadastro existente        |")
            print("| 3. Imprimir clientes cadastrados     |")
            print("| 4. Deletar um cadastro               |")
            print("| 5. Sair                              |")
            print('-' * 40)
            print()

            opcao = input("Opção: ")

            if opcao == "1":
                cpf = input("Digite o CPF do cliente: ")
                if cpf not in self.cadastro:
                    self.create(cpf)
                else:
                    print("Cliente já cadastrado.")

            elif opcao == "2":
                cpf = input("Digite o CPF do cliente que deseja alterar: ")
                self.update(cpf)

            elif opcao == "3":
                self.read()

            elif opcao == "4":
                cpf = input("Digite o CPF do cliente que deseja remover o cadastro: ")
                self.delete(cpf)

            elif opcao == "5":
                if self.sair():
                    break

            else:
                print("Opção inválida. Tente novamente.")


# Inicia o sistema
sistema = Sistema()
sistema.menu()
