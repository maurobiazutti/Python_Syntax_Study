# Variavel de Class
# Fica disponivel para todas as instancias(objetos) da class
class A:
    vc = 123 
    
a1 = A()
print(a1.vc) # Saída 123

a1.vc = 321
print(a1.vc) # Saída 321

a2 = A()
print(a2.vc) # Saída 123

print(A.vc) # Saída 123

A.vc = 654
print(a1.vc) # Saida 321
print(a2.vc) # Saida 654    
