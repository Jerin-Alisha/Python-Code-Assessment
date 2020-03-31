n=int(input("enter the numbers u want to print:"))
for i in range(1,n+1):
    if(i%3==0):
        print ('Fizz')
        continue
    elif(i%5==0):
        print ('Buzz')
        continue
    print i
    
	
