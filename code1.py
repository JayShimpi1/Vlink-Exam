n=int(input())
arr=[x for x in input().split(" ")]
if n <= 0:
	print("Invalid Input.")
else:
	arr.sort()
	print(arr)
	max=0
	output=""
	for i in arr:
		if len(i) > max:
			output=i
			max=len(i)
	print(output)