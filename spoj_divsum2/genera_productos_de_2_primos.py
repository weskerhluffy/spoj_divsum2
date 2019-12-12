# XXX: https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
with open('out', 'r') as myfile:
	data = myfile.read()
	# XXX: https://stackoverflow.com/questions/25253120/python-split-string-by-space-and-strip-newline-char
	nums=[s.strip() for s in data.split()]
#	print("AAA {}".format(nums))
	l1=[]
	l2=[]
	for i,n in enumerate(nums):
		if(i&1):
			l2.append(int(n))
		else:
			l1.append(int(n))
	r=[ns[0]*ns[1] for ns in zip(l1,l2)]
	for n in r:
		print(n)
