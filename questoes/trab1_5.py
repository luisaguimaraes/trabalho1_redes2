'''Trabalho Prático 1.
Grupo: Alessandro Luís Moreira
Gabriele Iara Ferreira
Luísa Vitória Guimarães Silva
Taylon Higor Pinheiro Costa
Tiago Mercês Rosário'''

#Importação da biblioteca que busca o retoro de uma url ou api.
from requests import get

#Definição da função que guarda o retorno da api ipify (essa api checa seu ip nat e o retorna)
# e imprime o ip na tela.
def ip_externo():
    print("\nQuestao 5: ")
    ip = get('https://api.ipify.org').text
    print('IP publico: ' + ip)