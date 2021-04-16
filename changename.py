import os
pathafter = 'C:\\Users\\N0868300\\Desktop\\ostest\\after'
pathorigin = 'C:\\Users\\N0868300\\Desktop\\ostest\\origin'
for root, dir, files in os.walk(pathorigin):
	for file in files:
		print(file.split('.')[0])
		filepath1 = os.path.join(pathorigin.replace('\\','\\\\'),file)
		filepath = os.path.join(pathafter.replace('\\','\\\\'),file)
		print(filepath1)
		print(filepath)
		os.system('copy %s '%filepath1+'%s' % filepath)
