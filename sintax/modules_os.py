# Para importar Bibliotecas = Modulos

import os # Permite interação com o Sitema Operacional

# # Manipulação de Arquivos e Diretórios:
# os.listdir() #:Lista os arquivos em um diretório.
# os.path.join() #: Concatena caminhos de diretórios de maneira adequada ao sistema operacional.
# os.mkdir() #: Cria um novo diretório.
# os.remove() #: Remove um arquivo.
# os.rmdir() #: Remove um diretório vazio.
# os.rename() #: Renomeia um arquivo ou diretório.

# # Execução de Comandos do Sistema:
# os.system() #: Executa um comando do sistema operacional.

# # # Variáveis de Ambiente:
# os.environ #: Um dicionário contendo as variáveis de ambiente do sistema.

# # # Caminho Atual:
# os.getcwd() #: Retorna o diretório de trabalho atual.

# # # Manipulação de Caminhos:
# os.path.exists() #: Verifica se um caminho existe.
# os.path.isfile() #: Verifica se um caminho aponta para um arquivo.
# os.path.isdir() #: Verifica se um caminho aponta para um diretório.



# # # Listar arquivos em um diretório
# arquivos = os.listdir('/caminho/do/diretorio')
# print(arquivos)

# # # Criar um diretório
# os.mkdir('/caminho/do/novo/diretorio')

# # # Verificar se um caminho existe
# if os.path.exists('/caminho/do/arquivo.txt'):
#     print("O arquivo existe!")

# # Obter o diretório de trabalho atual
# diretorio_atual = os.getcwd()
# print("Diretório atual:", diretorio_atual)



# Codigo para ler arquivos e organizar em suas respectivas pastas
lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

for nome_arq in lista_arquivos:
    if "txt" in nome_arq:
        if "22" in nome_arq:
            os.rename(f"arquivos/{nome_arq}", f"arquivos/22/{nome_arq}")
        elif "23" in nome_arq:
            os.rename(f"arquivos/{nome_arq}", f"arquivos/23/{nome_arq}") 
            


#Codigo que usei para mover arquivos .py para dentro da pasta sintax
lista = os.listdir()
# print(lista)

for nome in lista:
    if ".py" in nome:
        os.rename(nome, f"sintax/{nome}")