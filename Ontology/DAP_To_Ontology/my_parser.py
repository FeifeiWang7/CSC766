import sys
input = open(sys.argv[1], 'r')
output = open("output.txt", 'w')

prefix = "#"

namedIndividualList = []
propertyAssertionList = []

while 1:
	line = input.readline()
	if not line: break
	list = line.split(' ')
	print list	
	if(list[0] == '-'): continue
	else:
		namedIndividual = "namedIndividual('" + list[0] + "')."
		namedIndividualList.append(namedIndividual)

		length = len(list)
		
		loop = length/3
		i = 0
		for i in range(loop):
			if(list[i*3+1][0] == '9'): continue
			else:
				propertyAssertion = "propertyAssertion('MemoryAccessTime','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i*3+1] + "')))."
				propertyAssertionList.append(propertyAssertion)
				propertyAssertion = "propertyAssertion('L1CacheHit','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i*3+2] + "')))."
				propertyAssertionList.append(propertyAssertion)
				propertyAssertion = "propertyAssertion('L2CacheHit','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i*3+3] + "')))."
				propertyAssertionList.append(propertyAssertion)
				propertyAssertion = "propertyAssertion('OffChipMemoryAccessTime','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + str(int(list[i*3+1]) - int(list [i*3+2]) - int(list[i*3+3])) + "')))."
				propertyAssertionList.append(propertyAssertion)

for namedIndividual in namedIndividualList:
	output.write(namedIndividual+'\n')
for propertyAssertion in propertyAssertionList:
	output.write(propertyAssertion+'\n')
input.close()
output.close()
