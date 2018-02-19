import random

def getContentFile():
	zipfRes = open('./zipf_resource.txt','r')
	reslist = []
	for line in zipfRes:
		reslist.append(line)
	zipfRes.close()

	samples = random.sample(reslist,6)
	print samples

	contentFile = open('./content.txt','w')
	for s in samples:
		contentFile.write(s)
	contentFile.close()

if __name__ == '__main__':
    getContentFile()