#Scott Hansford
#CSC110 5/2/17

# variables: start (int), end (int), number (int)
# variables: flag(boolean), divisor (int)
import math
start=int(input("Enter the begin of the range >1: "))
endR=int(input("Enter the end of the range: "))
if endR>start and start>1:
    print("This is a list of prime numbers from",start,"to",endR)
    if start==2:
        print(start,end=" ")
    if start%2==0:      
        start+=1
    for number in range(start,endR+1,2):
        flag=True
        for divisor in range(3,int(math.sqrt(number))+1,2):
            if number%divisor==0:
                flag=False
                break
        if flag==True:
            print(number,end=" ")
else:
    print("Incorrect input")
