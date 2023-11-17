# public -> Podem ser acessados dentro e fora da class
# protected -> Podem ser acessados somente dentro da class ou filhas da class
# _protected 
# private -> Pode ser usada somente dentro da class
# __private (_NomeDaClass__nomeatributo) para acessar e modificar

class BaseDeDados:
    def __init__(self):
        self._dados = {}
       
        
    def inserir_cliente(self, id, nome):
        if 'cliente' not in self._dados:
            self._dados['cliente'] = {id: nome}
        else:
            self._dados['cliente'].update({id: nome})
            
    
    def lista_clientes(self):
        for id, nome in self._dados['cliente'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self._dados['cliente'][id]
        

# Instancia         
db = BaseDeDados()
db.inserir_cliente(1, 'Mauro')
db.inserir_cliente(2, 'João')
db.inserir_cliente(3, 'Marcos')

#print(db.dados)

db.apaga_cliente(2)
db.lista_clientes()
