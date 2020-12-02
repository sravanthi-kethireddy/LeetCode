def printChar(n):

	# print(chr(n))
	string = ''
	while n >0:
		n, i = divmod(n-1, 26)
		n = n%26
		print(n,i)
		string = chr(65 + i) + string
	return string

print(printChar(152))