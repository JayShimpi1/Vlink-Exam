def minChar(n,s):
	specialChar = 0
	digits = 0
	upperAlpha = 0
	lowerAlpha = 0

	for i in s:
		if (i == '!') or (i == '@') or (i == '#') or (i == '$') or (i == '%'):
			specialChar += 1
		elif (ord(i) >= 48) and (ord(i) <= 57):
			digits += 1
		elif i.isupper():
			upperAlpha += 1
		elif i.islower():
			lowerAlpha += 1
		else:
			pass

	newNumbers = 0
	
	print("Password contains:")
	print("Special characters :", specialChar)
	print("Digits :",digits)
	print("Upper Alphabets : ",upperAlpha)
	print("Lower Alpabets : ",lowerAlpha)
	
	if specialChar == 0:
		newNumbers+=1
	if digits == 0:
		newNumbers+=1
	if upperAlpha == 0:
		newNumbers+=1
	if lowerAlpha == 0:
		newNumbers+=1

	if n >= 8 and newNumbers == 0:
		print("Strong Password, Good to Go!")
	elif n>=8:
		print(newNumbers," more characters should be added.")
	else:
		total = n+newNumbers
		if total<8:
			print(total+(8-total), " more characters should be added.")
		else:
			print(total, " more characters should be added.")

n = int(input())
s = input()
minChar(n,s)