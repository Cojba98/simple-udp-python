from socket import *


# Staticke varijable
server_address = 'localhost'
server_port = 8090

# Pravljenje soketa - AF_INET za IPv4 protokol, SOCK_STREAM za TCP protokol
srv_socket = socket(AF_INET, SOCK_DGRAM)

# Vezujemo napravljeni socket za svoju adresu, kao i za port na kom ce da slusa
srv_socket.bind( (server_address, server_port) )

while True:
    # Prihvata recenicu koju je klijent poslao
    sentence, client_address = srv_socket.recvfrom(1024)
    print('I received a new request! Processing this sentence:', sentence)

    # Obradjuje recenicu
    sentence = sentence.decode()  # decode() da bismo prebacili iz bajtova u string
    sentence = sentence[::-1]  # Obrcemo recenicu - [ start : end : step ]
    # Obzirom da celu recenicu hocemo unazad, start i end ostavljamo prazno, a step stavljamo na -1 (po jedno slovo, u levo)

    #Salje recenicu nazad
    srv_socket.sendto(sentence.encode(), client_address )

'''
Skraceni zapis ovog servera:

from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', 8090))

while True:
    sentence, client_address = sock.recvfrom(1024)
    sock.sendto(sentence.decode()[::-1].encode(), client_address)

'''