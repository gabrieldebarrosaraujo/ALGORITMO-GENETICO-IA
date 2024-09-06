import random
from ag import AlgoritmoGenetico
import datetime


def funFitness(genes, dados):
    
    chute = [dados[g] if isinstance(g, int) else g for g in genes]
    return descubraPalavra(chute)

def criaIndividuo(dados):
    return [random.choice(dados) for _ in range(5)]


def descubraPalavra(chute):
    chute = ''.join(chute[0:5])
    palavras = ['termo', 'nobre', 'sobre', 'poder', 'etnia', 'haver', 'corte', 'pular', 'digna', 'ceifa', 'lento', 'tumba', 'xampu', 'torre', 'lapis', 'sagaz', 'expor', 'anexo', 'teste']

    dia = datetime.datetime.today().day
    index = dia % len(palavras)

    pontos = 0
    for i in range(len(palavras[index])):
        
        if chute[i] in palavras[index]:
            pontos += 1
        
        if chute[i] == palavras[index][i]: 
            pontos += 1

    return pontos


letras = list("abcdefghijklmnopqrstuvwxyz")


ag = AlgoritmoGenetico(
    dados=letras,
    tamPopulacao=50,
    limGeracoes=500,
    probMutacao=5,
    funcaoFitness=funFitness,
    maiorFitness=True
)


ag.funCriaIndividuo = criaIndividuo


ag.executa()


palavra_proxima = ag.melhorResultado()
print(f"Palavra mais próxima: {''.join(palavra_proxima['genes'])}, Fitness: {palavra_proxima['fitness']}")
