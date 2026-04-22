import socket
import datetime
import braocast

server_add = "192.168.1.4"
port =9999
buffersize = 1024
colletion  = (server_add ,port )
n = 0

"""
dict format :- 
  Ip : [port , messages  , number of times repeating]
"""
myDict = {}


# bind the port numer and the host name
s = socket.socket(family=socket.AF_INET , type = socket.SOCK_DGRAM)
s.bind((server_add,port))
print(f"listening to the loopback address:{server_add} at port number: {port}")




while n<1:
  msg , client_add = s.recvfrom(buffersize)
  ip = client_add[0]
  port = client_add[1]
  message = msg.decode()
  
  # creating the dict 
  if port in myDict:
    myDict[port][0][1] += msg.decode()
    myDict[port][0][2] +=1
  else:
    myDict[client_add[1]] = [[client_add[0] , [msg] , 1]]
  
  # data
  print("Received:-",msg.decode())
  print("ip-:",client_add[0])
  print("port:-:",client_add[1])

  finalMsg = msg.decode()
  s.sendto(finalMsg.encode() , client_add)
  n+=1 

print(myDict)
s.close()


