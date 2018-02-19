import sys,getopt
import math

# test commend
# the zipf destribution simulation
def zipf():
	opts,args = getopt.getopt(sys.argv[1:],"p:n:",["help"])

	num = 5000

	for opt, args in opts:
		if opt in ("-p"):
			s = float(args)

	sum_n=0
	fff = open('./number.txt','w')
	for i in range(num):
		delt = 1/((i+1)**s)
		sum_n = sum_n + delt
		fff.write(str(delt*50000)+'\n')
		

	fff.close()
	p_list = []
	for i in range(num):
		prob = (1/((i+1)**s))/sum_n
		print prob
		p_list.append(prob)




if __name__ == '__main__':
    zipf()
    printf("success!")
