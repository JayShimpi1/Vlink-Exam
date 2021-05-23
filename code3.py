import math

def isPrime(num):
	if num > 1:
	    for i in range(2, int(num/2)+1):
	        if (num % i) == 0:
	            return False
	            break
	    else:
	        return True
	 
	else:
	    return False

def primeFactors(n):
    arr = []
    while n % 2 == 0:
    	arr.append(2)
    	n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
        	arr.append(int(i))
        	n = n / i
    if n > 2:
    	arr.append(int(n))

    return arr

n = int(input())
if len(str(n)) == 1:
	print("Invalid number")
elif isPrime(n):
	print("Please input a diffrent number")
else:
	output = primeFactors(n)
	output = sorted(output, reverse=True)
	print(output)
	product = 1
	for i in output:
		product *=i
	print(product)
