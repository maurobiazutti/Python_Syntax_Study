# While 

#Exemplo de uso do While: 
#Numeros impares ate 50
num = 1
while num <= 50:
    if num % 2 == 1:
        print(num)
    num += 1
  
 ######################################################################### 
  
# Exemplo de uso do While:    
produto = []
    
while True:
    cadastro_produto = input("Cadastre um Produto.")
    cadastro_produto = cadastro_produto.lower()
    
    if cadastro_produto == "sair":
        break  # logica para sair do Loop While
    
    
    if cadastro_produto in produto:
        print("Produto já cadastrado")
    else:
        print(f"Produto {cadastro_produto} cadastrado com sucesso!")
        produto.append(cadastro_produto)
        
    print(produto)
    
 ######################################################################### 
 
 