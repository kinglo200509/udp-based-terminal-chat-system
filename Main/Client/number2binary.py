
# function to convert 
def convertion(numb):
  string  =""
  while numb!=0:
    # checking condition

    
    reminder= numb % 2 
    
    string = f"{string}{reminder}"
    numb = numb//2 
    print(numb)
  return string[::-1]




def binary(ip):
  converted_ip =  "" 
  array_strings = ip.split(".")
  for number in array_strings:
    result=convertion(int(number))
    # return in string 
    # not flips the truth table and empty string is false
    if not converted_ip:
      converted_ip += f"{result}"
    else:
      converted_ip += f".{result}"
    

  print(converted_ip)



  
