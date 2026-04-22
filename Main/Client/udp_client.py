import socket
import broadcast

# creating an udp socket  
udpSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# client Detials
ip_int = socket.gethostname()
ip_add  = socket.gethostbyname(ip_int)

# detials
broadcast.broacdcastFunc(ip_add , )
collection = (server_add , port)


# bind
udpSocket.bind((ip_add , 0))




while True:
  # sending data to the server
  msg = input("What to send:- ")

  # sending to server
  udpSocket.sendto(msg.encode() ,collection)

  # recv message and decode herer 1024 is buffer size 
  recvMsg , ServerAdd = udpSocket.recvfrom(1024)

  print(f"This is the received msg:-{recvMsg} ")
  print(f"This is the Server Address:-{ServerAdd} ")





