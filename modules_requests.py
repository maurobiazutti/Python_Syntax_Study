import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

#Para pegar uma informação
resposta = requests.get(link)
# print(resposta) # Saida <Response [200]> | sucesso requisição foi bem sucedida. 

dicionario_resposta = resposta.json()
# print(dicionario_resposta) Saída Todas as cotações
# print(dicionario_resposta["USDBRL"]) Saída cotação Dolar x BRL
# print(dicionario_resposta["BTCBRL"]) Saida cotação Bitcoin x BRL

cotacao_dolar = dicionario_resposta["USDBRL"]
print(cotacao_dolar["bid"])

cotacao_bitcoin = dicionario_resposta["BTCBRL"]
print(cotacao_bitcoin["bid"])


