# Tratamendo_de_String

texto_01 = "Minha vagas já esta GARANTIDA"

#len() tamanho da STR
tamaho_str = len(texto_01)
print(tamaho_str) # Saída 29

#Maiuscula e Minusculo
minusculas = texto_01.lower()
maiusculas = texto_01.upper()
print(minusculas)
print(maiusculas)

#strip(): Remove espaços em branco no início e no final da string.
texto_02 = "    Minha vagas já esta GARANTIDA"
texto_sem_espaco = texto_02.strip()
print(texto_sem_espaco)


#split(): Divide a string em substrings com base em um delimitador.
texto_03 = "Minha, vagas já esta, GARANTIDA"
texto_04 = "Minha - vagas - já esta - GARANTIDA"
palavras_01 = texto_03.split(",") #Saida ['Minha', ' vagas já esta', ' GARANTIDA']
palavras_02 = texto_04.split("-") #Saída ['Minha ', ' vagas ', ' já esta ', ' GARANTIDA']
print(palavras_01)
print(palavras_02)

#join(): Junta elementos de uma lista em uma única string usando um separador.
palavras_02 # ['Minha ', ' vagas ', ' já esta ', ' GARANTIDA']
texto_05 = ''.join(palavras_02)
print(texto_05) #Saída Minha  vagas  já esta  GARANTIDA

#replace(): Substitui uma substring por outra.
novo_texto = texto_01.replace("vagas", "Emprego")
print(novo_texto) #Saída Minha Emprego já esta GARANTIDA

#startswith() e endswith(): Verifica se a string começa ou termina com uma determinada substring.
comeca_com = texto_01.startswith("Minha")
termina_com = texto_01.endswith("GARANTIDA")
print(comeca_com) #Saída True
print(termina_com) #Saída True


#find() e index(): Procuram a primeira ocorrência de uma substring na string. 
# A diferença é que find() retorna -1 se não encontrar, enquanto index() levanta uma exceção.
posicao_01 = texto_01.find("vagas")
print(posicao_01) #Saída 6

posicao_02 = texto_01.find("G")
print(posicao_02) #Saída 20

posicao_03 = texto_01.find("Y")
print(posicao_03) #Saída -1

posicao_01 = texto_01.index("vagas")
print(posicao_01) #Saída 6

posicao_02 = texto_01.index("G")
print(posicao_02) #Saída 20

#posicao_03 = texto_01.index("Y")
# print(posicao_03) #Saída  posicao_03 = texto_01.index("Y") ValueError: substring not found

#isdigit() Verificam se a string é de numeros
numerico = "123"
print(numerico.isdigit()) #Saída True

#isalpha() Verificam se a string é de letras
alfabetico = "abc"
print(alfabetico.isalpha()) #Saída True

#isalnum() Verificam se a string é de alfanuméricos
alfanumerico = "abc123"
print(alfanumerico.isalnum()) #Saída True


