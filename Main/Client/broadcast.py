import socket

# broadcast messages
def broacdcastFun():
  braocastsocket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
  # enabling broadcast and setting the same port number
  braocastsocket.setsockopt(socket.SOL_SOCKET , socket.SO_BROADCAST , 1 )
  braocastsocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1 )

# bindd to all interface
  broadcast_add = ""
  port_number =10000
  braocastsocket.bind((broadcast_add , port_number))
  print(f"listening to broadcast")
  RecvBroacastMsg , RecvIp = braocastsocket.recvfrom(1024)
  
  # data
  print(f"This is the message: {RecvBroacastMsg}")
  print(f"This is the IP: {RecvIp[0]}")
  print(f"This is the port: {RecvIp[1]}")

broacdcastFun()