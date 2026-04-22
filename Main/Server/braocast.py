import socket


def broadcastFucn():
  broadcast =  socket.socket(family=socket.AF_INET , type=socket.SOCK_DGRAM)
  broadcast.setsockopt(socket.SOL_SOCKET , socket.SO_BROADCAST , 1)
  
  # broadcast add 
  broadcast_add = "192.168.1.255"
  port = 10000
  message = "TO extract the IP address"
  
  print(f"sending broadcast message.")
  broadcast.sendto(message.encode() , (broadcast_add,port))
  
  recv_msg , clientInfo = broadcast.recvfrom(1024)
  if clientInfo[1] == myDict:
    myDict[clientInfo[2]] +=1
    myDict[clientInfo[1]] += message.encode()
  else:
    myDict[clientInfo[1]] = [clientInfo[0] , [recv_msg] , 0]
