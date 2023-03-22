word="kajak"
word=word.lower()
z=[*word]
if ' ' in z:
	z.remove(' ')
w=0
for x in range(len(z)//2):
	if z[x]==z[-x-1]:
		w=w+1
	else:
		print(z[x],'=/=',z[-x-1])
		w=0
if w==len(z)//2:
	print(word, 'to palindrom')
else:
	print(word, 'nie jest palindromem')