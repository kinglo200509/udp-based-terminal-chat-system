import socket

#  ip of the host
hostname = socket.gethostname()
ip_add = socket.gethostbyname(hostname)
print(f"This is the ip of the host: {ip_add}")

# server_detials
server_ip = hostname

# collection - use 0.0.0.0 to let system choose interface
collection = ("0.0.0.0" , 0)

# socket
udpSocket = socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)

# bind to specific IP (assign user IP), let system choose port
udpSocket.bind(collection)

# server address
server_info = ("192.168.56.1", 9999)

# connting to server
while True:

  msg = input("Type your input:- ")

  # senidng the msg to server
  udpSocket.sendto( msg.encode(),server_info)

  # recv msg
  reply_msg , server_info = udpSocket.recvfrom(1024)
  
  # info received
  print(f"reply_message:- ({reply_msg.decode()}) ")
  print(f"server_ip:- ({server_info[0]}) ")
  print(f"server_port_no:- ({server_info[1]}) ")
  


  
