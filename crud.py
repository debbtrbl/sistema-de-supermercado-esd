class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

class Produto:
    def __init__(self, id_produto, nome, tipo, categoria, valor, validade):
        self.id_produto = id_produto
        self.nome = nome
        self.tipo = tipo
        self.categoria = categoria
        self.valor = valor
        self.validade = validade

clientes = []
produtos = []

# Funções Cliente
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

# Funções Produto
def cadastrar_produto(id_produto, nome, tipo, categoria, valor, validade):
    produto = Produto(id_produto, nome, tipo, categoria, valor, validade)
    produtos.append(produto)

def listar_produtos():
    for produto in produtos:
        print(f"ID: {produto.id_produto}, Nome: {produto.nome}, Tipo: {produto.tipo}, Categoria: {produto.categoria}, Valor: {produto.valor}, Validade: {produto.validade}")

def deletar_produto(id_produto):
    global produtos
    produtos = [produto for produto in produtos if produto.id_produto != id_produto]

def atualizar_produto(alt_id_produto, alt_nome, alt_tipo, alt_categoria, alt_valor, alt_validade):
    for produto in produtos:
        if produto.id_produto == alt_id_produto:
            produto.nome = alt_nome
            produto.tipo = alt_tipo
            produto.categoria = alt_categoria
            produto.valor = alt_valor
            produto.validade = alt_validade