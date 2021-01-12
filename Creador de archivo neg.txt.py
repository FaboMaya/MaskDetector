import os

i = 0

with open("neg.txt","w") as f:
	for filename in os.listdir('Background'):
		i +=1
		f.write('Background/' + filename + '\n')
		if i == 100:
			break