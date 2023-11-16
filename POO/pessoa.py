from datetime import datetime

# Class
# Toda class tem Atributos e Metodos
class Pessoa:
    # Variavel de class
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        # variavel de instancia
        self.nome = nome
        self.idade = idade
        self.comendo = False
        self.falando = False
        
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return # Se a condição for verdadeira a execução para por aki
        
        if self.falando:
            print(f'{self.nome} não pode comer enquanto estiver falando.')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando sobre {assunto}.')
            return
        
        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True
        
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False
        
    def get_ano_nascimendo(self):
        print(self.ano_atual - self.idade)
        return 
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

 