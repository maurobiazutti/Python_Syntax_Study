class MinhaClasse:
    def meu_metodo(self):
        print("Olá, eu sou um método!")
        
    
    def meu_metodo2(self, num, mul):
        return num * mul
    

objeto = MinhaClasse()
objeto.meu_metodo()
result = objeto.meu_metodo2(2, 5)
print(result)