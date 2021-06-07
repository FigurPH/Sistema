class Produto:

    # definição do inicializador
    def __init__(self, id, barcode, nome, preco, desc, cat, qtd):
        self.id = id
        self.barcode = barcode
        self.nome = nome
        self.preco = preco
        self.desc = desc
        self.cat = cat
        self.qtd = qtd

    def dump(self):
        print("ID: ", self.id,"|",
              "Nome: ", self.nome,"|",
              "CódBarras: ", self.barcode,"|",
              "Preço: ", self.preco,"|",
              "Desc: ", self.desc,"|",
              "QTD: ", self.qtd,"|",
              "Catg: ", self.cat)