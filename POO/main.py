# Importe da Class Pessoa
from pessoa import Pessoa

# Instanciando (criando) um objeto
p1 = Pessoa('Mauro', 36)
print(p1) # Saída <pessoa.Pessoa object at 0x7f872f9efc10>
print(p1.nome) # Saída Mauro
print(p1.idade) # Saída 36

p1.falar("Programação") # Mauro esta falando sobre Programação
p1.parar_falar()
p1.comer('picanha')
p1.falar('tecnologia')
p1.parar_comer()
p1.comer('pizza')
print(p1.get_ano_nascimendo())