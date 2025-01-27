class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

clientes = []

def cadastrar_cliente(cpf, nome, endereco):
    cliente = Cliente(cpf, nome, endereco)
    clientes.append(cliente)

def listar_clientes():
    for cliente in clientes:
        print(f"CPF: {cliente.cpf}, Nome: {cliente.nome}, Endereço: {cliente.endereco}")

def deletar_cliente(cpf):
    global clientes
    clientes = [cliente for cliente in clientes if cliente.cpf != cpf]

def atualizar_cliente(alt_cpf, alt_nome, alt_endereco):
    for cliente in clientes:
        if cliente.cpf == alt_cpf:
            cliente.nome = alt_nome
            cliente.endereco = alt_endereco