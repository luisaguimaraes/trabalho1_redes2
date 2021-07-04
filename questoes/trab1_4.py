'''Trabalho Prático 1.
Grupo: Alessandro Luís Moreira
Gabriele Iara Ferreira
Luísa Vitória Guimarães Silva
Taylon Higor Pinheiro Costa
Tiago Mercês Rosário'''

#Importação da biblioteca que busca o endereço físico. Importante: biblioteca externa ao Python,
# requer instalação via Pip!
from getmac import get_mac_address

#Definição da função que pega o retorno da biblioteca get_mac_address e imprime na tela.
def get_mac():
    print("\nQuestao 4: ")
    mac = get_mac_address()
    print ("Endereco MAC: " + mac)