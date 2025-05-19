# polimorfismo = A mesma função ter muitas formas
#Ex: são funções capaz de executar contextos diferentes,  exemplo   o len() que conta caracteres em string ou conta quantos itens tem em uma lista



class passaro:
    def voar(self):
             print("voando...")


class pardal(passaro):
       def voar(self):
            super().voar() #aqui eu estou fazendo uso da propria função do voar() da classe passaro para o pardal

class avestruz(passaro):
    def voar(self):
        print("Avestruz não voa")#aqui eu estou passando contexto diferente para o avestruz (fazendo tratamento diferente), haja vista que avestruz não voa


def plano_voo(obj):
      obj.voar()#eu crio essa função que chama voar() 

p1 = pardal()
p2 = avestruz()

#plano_voo(p1)#chamo a função que chama voo (que para o pardal vai funcionar como padrão)
plano_voo(p2)#para o avestruz, como foi estipulado contexto diferente, a função plano_voo() não retornara o resultado padrão de voar(), visto que apliquei método diferente de retorno (isso é polimorfismo)