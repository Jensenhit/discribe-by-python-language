fl = open('cvbf.txt','r')
f2 = open('cvbf.enw','w')
for lines in fl.readlines():
	ib = 'z'
	flag = 0
	f2.write('%0 Conference Proceedings\n%A  ')
	for i in lines:
		if i == ',':
			if ib.islower():
				f2.write('\n%A  ')
			else:
				f2.write('\n%D  ')
		elif ib.islower() and i == '.' and flag == 0:
			f2.write('\n%T  ')
			flag = 1
		elif ib.islower() and i == '.' and flag == 1:
			f2.write('\n%B  ')
		elif i == '\t': 
			f2.write('\n\n')
			break
		else:
			f2.write(i)
		ib = i
fl.close()
f2.close()
