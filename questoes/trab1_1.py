'''Trabalho Prático 1.
Grupo: Alessandro Luís Moreira
Gabriele Iara Ferreira
Luísa Vitória Guimarães Silva
Taylon Higor Pinheiro Costa
Tiago Mercês Rosário'''

#Importação da biblioteca que faz uma requisição à uma url.
import urllib.request

#Definição de uma função, na qual, através de um comando try, tenta fazer uma requisição ao Google e, caso
# a requisição seja bem sucedida, retorna uma mensagem "Conectado a Internet!" e, caso haja excessão, retorna
#a mensagem "Sem Internet!"

def checa_conexao():
    print("\nQuestao 1: ")
    try:
        urllib.request.urlopen('http://google.com')
        print("Conectado a intetnet!")
    except Exception as e:
        if (type(e).__name__ == 'URLError'):
            print('Sem internet')
