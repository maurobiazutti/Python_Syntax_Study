# Tuplas in Python
# Uma tupla (tuple) é uma sequência ordenada e imutável de elementos.

# Criando uma tupla
minha_tupla = (1, 2, 3, 'a', 'b')

# Acessando elementos da tupla
print(minha_tupla[0])  # Saída: 1
print(minha_tupla[3])  # Saída: 'a'

# Iterando sobre uma tupla
for elemento in minha_tupla:
    print(elemento)

# Comprimento da tupla
print(len(minha_tupla))  # Saída: 5


def calcular_impostos2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

resposta = calcular_impostos2(1000) # Saida (275.0, 35.0, 50.0)
print(resposta) # Saida (275.0, 35.0, 50.0)

#Tambem posso receber os valores da tupla atribuindo a variaveis
ir, csll, iss = calcular_impostos2(1000)
print(ir, csll, iss, sep="\n")

print(resposta[0]) # Saida 275.0
print(resposta[1]) # Saida 35.0
print(resposta[2]) # Saida 50.0





 
 