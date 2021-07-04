'''Trabalho Prático 1.
Grupo: Alessandro Luís Moreira
Gabriele Iara Ferreira
Luísa Vitória Guimarães Silva
Taylon Higor Pinheiro Costa
Tiago Mercês Rosário'''

#Importação das requisições que checam o tempo de conexão
import requests

#Definição de uma função, a qual vai checar o tempo total que foi necessário para acessar a url do Google.
def checatempo():
    print("\nQuestao 2: ")
    conexao = requests.post('http://google.com.br')
    print(conexao.elapsed.total_seconds())