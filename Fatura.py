class Fatura:
    #def define funções e métodos
    def __init__(self, numero_item, descricao_item, quantidade, preco_unitario): #Método init (construtor) da classe Fatura
        self.numero_item = numero_item
        self.descricao_item = descricao_item
        self.quantidade = quantidade if quantidade > 0 else 0
        self.preco_unitario = preco_unitario if preco_unitario > 0 else 0.0

    def set_numero_item(self, numero_item): #self é o proprio objeto do construtor
        self.numero_item = numero_item

    def get_numero_item(self):
        return self.numero_item

    def set_descricao_item(self, descricao_item):
        self.descricao_item = descricao_item

    def get_descricao_item(self):
        return self.descricao_item

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade if quantidade > 0 else 0

    def get_quantidade(self):
        return self.quantidade

    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario if preco_unitario > 0 else 0.0

    def get_preco_unitario(self):
        return self.preco_unitario

    def get_fatura(self):
        return self.quantidade * self.preco_unitario

# Mapeamento de produtos
produto = None
valor = 0.0
produtos = {
    123: {
        'descricao_item': 'Teclado Mecânico Gamer HyperX Alloy MKW100, RGB, Switch Red, Full Size, US, Preto',
        'numero_item': produto,
        'preco_unitario': valor
    },
    456: {
        'descricao_item': 'Mouse Gamer Logitech G203 Lightsync, RGB, 8000 DPI, Preto',
        'numero_item': produto,
        'preco_unitario': valor
    },
    789: {
        'descricao_item': 'Placa de Vídeo Gigabyte NVIDIA GeForce GTX 1660 OC, 6GB, GDDR5 - GV-N1660OC-6GD',
        'numero_item': produto,
        'preco_unitario': valor
    },
    321: {
        'descricao_item': 'SSD Kingston A400, 1TB, SATA, Leitura 500MB/s, Gravação 450MB/s - SA400S37/960G',
        'numero_item': produto,
        'preco_unitario': valor
    },
    654: {
        'descricao_item': 'HD Seagate Barracuda, 1TB, 3.5, SATA - ST1000DM010',
        'numero_item': produto,
        'preco_unitario': valor
    },
    987: {
        'descricao_item': 'Fonte Cooler Master MWE 500W, 80 Plus White, PFC Ativo, 110V - MPW-5002-ACABW',
        'numero_item': produto,
        'preco_unitario': valor
    }
}

while True:
    try:
        produto = int(input('\nGerar fatura de qual produto? \n[123] Teclado\n[456] Mouse\n[789] Placa de video\n[321] SSD 1TB\n[654] HD 1TB\n[987] Fonte 500w\nNúmero do produto: '))
        if produto in produtos: # Verifica se o produto existe na lista de produtos
            descricao_item = produtos[produto]['descricao_item'] # Atribui a descrição do produto
            numero_item = produto # Atribui o número do produto
            try:
                valor = float(input('Preço do produto: '))
            except ValueError:
                print('Entrada inválida. Insira um valor válido.')
                continue  # Volte ao início do loop se a entrada for inválida

            preco_unitario = valor
        else:
            print('Opção inválida, tente novamente.')
            continue  # Volta ao início do loop se a escolha for inválida
    except ValueError:
        print('Entrada inválida. Insira um número válido.')
        continue  # Volta ao início do loop se a entrada for inválida

    try:
        quantidade = int(input('Quantos produtos você deseja? '))
    except ValueError:
        print('Entrada inválida. Insira um número válido.')
        continue  # Volta ao início do loop se a entrada for inválida

    # Gerar fatura
    fatura = Fatura(numero_item, descricao_item, quantidade, preco_unitario) #Atribuindo a estancia da classe Fatura para a váriavel fatura
    print(f"\nFatura:\n * Número do produto: {fatura.get_numero_item()}\n * Descrição: {fatura.get_descricao_item()}\n * Quantidade: {fatura.get_quantidade()}\n * Preço unitário: {fatura.get_preco_unitario()}\n * Valor: R$ {fatura.get_fatura():.2f}")

    resposta = input('\n[F] Criar outra fatura\n[S] Sair\nEscolha: ')
    if resposta.upper() == 'S':
        print('Saindo...')
        break  # Sai do loop principal
    elif resposta.upper() == 'F':
        continue  # Volta ao início do loop principal
