'''Trabalho Prático 1.
Grupo: Alessandro Luís Moreira
Gabriele Iara Ferreira
Luísa Vitória Guimarães Silva
Taylon Higor Pinheiro Costa
Tiago Mercês Rosário'''

#Importação da biblioteca que faz a interface dos sockets para o Python.
import socket

#Definição da função que busca o nome do host e do ip locais.
def ip_info():
    print("\nQuestao 3: ")
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    print("host: " + host + "\nIP: " + ip)
