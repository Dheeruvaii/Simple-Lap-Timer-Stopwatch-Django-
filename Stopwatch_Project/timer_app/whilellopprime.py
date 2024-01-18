n=7
if n > 1:
    for  i in range(2,int(n/2)+1):
        if (n%i)== 0:
            print(n, "is not a prime number")
            break
        else:
            print(n, "is a prime number")
    # If the number is less than 1, its also not a prime number.
    else:
            print(n, "is not a prime number")
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")