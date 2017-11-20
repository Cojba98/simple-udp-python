from socket import *

# Staticke varijable
server_address = 'localhost'
server_port = 8090

# Cekamo unos sa tastature
sentence = input('Unesi neku recenicu')

# Pravljenje soketa - AF_INET za IPv4 protokol, SOCK_DGRAM za UDP protokol
cl_socket = socket(AF_INET, SOCK_DGRAM)

# Saljemo recenicu serveru
cl_socket.sendto(sentence.encode(), (server_address, server_port))

# Prihvatamo recenicu (i odmah je prikazujemo u konzoli)
# [0] stoji tu da oznaci prvi element tuple-a (para), obzirom da metoda
# recvfrom() vraca podatke, kao i adresu posiljaoca
print(cl_socket.recvfrom(4096)[0].decode())

'''
Skraceni zapis ovog klijenta:

from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(input('Unesi neku recenicu').encode(), ('localhost', 8090))
print(sock.recvfrom(4096)[0].decode())
'''