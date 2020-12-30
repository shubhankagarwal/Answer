

def getSum(n):  
     
    sum = 0
    for digit in str(n):   
      sum += int(digit)        
    return sum
count = 0
total = 0
while True:
  no = input("enter the guess: " )
  if no == "notmore":
    
    break

  try :
    nu = int(no)
    
  except:
    continue

total=getSum(nu)
print("total ",total)
while(nu>0):
    count=count+1
    nu=nu//10
print("the count is ",count)

avg = total/count
print("avg",avg)
