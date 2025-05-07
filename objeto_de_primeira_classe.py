def somar(a , b):    
    return  (a + b),"+"

def subtracao(a , b):    
    return  (a - b),"-"
 
 
#a função a abaixo receb valores e pergunta qual função será utilizada, no caso a função somar()
def mostra_resultado_personalizado(a, b, funcao_somar):
    vetor= funcao_somar(1 , b)


    print(f"o valor da operação {a} {vetor[1]} {b} = {vetor[0]} ")



mostra_resultado_personalizado(1,1,somar)
mostra_resultado_personalizado(1,1,subtracao)
