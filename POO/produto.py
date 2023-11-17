class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        
    # GETTER  
    @property
    def preco(self):
        return self._preco
    
    # SETTER
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor        
        
    
pr1 = Produto('Camisa', 50)
pr1.desconto(10)
print(pr1.preco)
    
pr2 = Produto('copo', "R$20")
pr2.desconto(20)
print(pr2.preco)
        
        