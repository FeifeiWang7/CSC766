import sys
file = open(sys.argv[1], 'r')
output = open("output.txt", 'w')

while 1:
	line = file.readline()
	if not line: break
	name = line[:max(line.find(' '), 0) or None]
	namedIndividual = "namedIndividual('" + name + "')."
	output.write(namedIndividual)
	output.write('\n')
file.close()
output.close()
