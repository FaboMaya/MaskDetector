import os

negs = 0
samples = 786
bgs = len(os.listdir("Background/"))
step = (bgs*2)//samples

with open("neg.txt","w") as f:
	fileList = os.listdir('Background')
	for index in range(0,bgs,step):
		f.write('Background/' + fileList[index] + '\n')
		negs += 1

print("Negs: {0} \nSamples: {1} \nBgs: {2} \nStep: {3}".format(negs,samples,bgs,step) )