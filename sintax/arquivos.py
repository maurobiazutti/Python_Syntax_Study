# Função para abrir arquivos
# w -> write mode de escrita
# r -> read mode leitura
 
# # Para abrir o arquivo
# arquivo = open("vendas.txt", "w")

# # Aki posso fazer o que quiser com o  arquivo

# # Para fechar o arquivo
# arquivo.close()


# Neste formato abre, fecha e guarda os dados na variavel arquivo
with open("vendas.txt", "r") as arquivo:
    # Aki posso fazer o que quiser com o  arquivo
    
    # informacoes = arquivo.read()
    
    info = arquivo.readlines()
    # print(info)
    
# Tratando dados
total_vendas = 0
for item in info:
    item = item.replace("\n", "") 
    #print(item)
    item = item.replace(" ", "")
    #print(item)
    separar = item.split(",")   
    #print(separar) 
    valor = separar[1]
    #print(valor)
    valor = float(valor)
    #print(valor)
    total_vendas += valor

print(f"Volor total de vendas é de R${total_vendas:,.2f}")


