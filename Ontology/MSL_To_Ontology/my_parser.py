import sys
input = open(sys.argv[1], 'r')
output = open("output.txt", 'w')

prefix = "#"

namedIndividualList = []
propertyAssertionList = []
classAssertionList = []

processor = "M2075"
namedIndividualList.append("namedIndividual('" + prefix + processor + "').")
namedIndividualList.append("namedIndividual('" + prefix + processor + "Processor').")
propertyAssertion = "propertyAssertion('" + prefix + "consistsOf','" + prefix + processor + "','" + prefix + processor + "Processor')."
propertyAssertionList.append(propertyAssertion)

classAssertion = "classAssertion('" + prefix + "Tesla" + "','"+ prefix + processor + "')."
classAssertionList.append(classAssertion)
classAssertion = "classAssertion('" + prefix + "Processor" + "','" + prefix + processor + "Processor')."
classAssertionList.append(classAssertion)

textualMemoryCount = 65

while 1:
	i = 0
	line = input.readline()
	if not line: break
	list = line.split(' ')

	if(list[0] == "die"): 
		namedIndividualList.append("namedIndividual('" + prefix + "block').")
                namedIndividualList.append("namedIndividual('" + prefix + "core').")
                namedIndividualList.append("namedIndividual('" + prefix + "die').")
                namedIndividualList.append("namedIndividual('" + prefix + "grid').")
                namedIndividualList.append("namedIndividual('" + prefix + "sm').")
                namedIndividualList.append("namedIndividual('" + prefix + "tpc').")
                namedIndividualList.append("namedIndividual('" + prefix + "warp').")

		propertyAssertion = "propertyAssertion('" + prefix + "numberOfDiesValue','" + prefix + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + "1" + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('" + prefix + "TPCPerDie','" + prefix + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[2] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('" + prefix + "SMPerTPC','" + prefix + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[6] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('" + prefix + "CoresPerSM','" + prefix + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[10] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('" + prefix + "membus','" + prefix + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[14] + "')))."
		propertyAssertionList.append(propertyAssertion)

		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "block')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "core')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "die')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "grid')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "sm')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "tpc')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('" + prefix + "scope','" + prefix + "warp')."
		classAssertionList.append(classAssertion)
		
		continue

	if(list[0] == "globalMem"):
		namedIndividual = "namedIndividual('" + prefix + processor + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "GlobalMemory','" + prefix + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
		list[0] = "M2075globalMem"
	elif(list[0] == "L1"):
		namedIndividual = "namedIndividual('" + prefix + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "Cache','" + prefix + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "L2"):
		namedIndividual = "namedIndividual('" + prefix + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "Cache','" + prefix + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "constantMem"):
		namedIndividual = "namedIndividual('" + prefix + processor + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "ConstantMemory','" + prefix + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
		list[0] = "M2075constantMem"
	elif(list[0] == "cL1"):
		namedIndividual = "namedIndividual('" + prefix + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "L1_constant','" + prefix + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "cL2"):
		namedIndividual = "namedIndividual('" + prefix + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "L2_constant','" + prefix + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "readonlyMem"):
		namedIndividual = "namedIndividual('" + prefix + processor + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "ReadOnlyMemory','" + prefix + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
		list[0] = "M2075readonlyMem"
	elif(list[0] == "sharedMem"):	
		namedIndividual = "namedIndividual('" + prefix + processor + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "SharedMemory','" + prefix + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
		list[0] = "M2075sharedMem"
	elif(list[0] == "tL1"):
		namedIndividual = "namedIndividual('" + prefix + list[0] + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "L1_texture','" + prefix + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "textureMem"):	
		namedIndividual = "namedIndividual('" + prefix + processor + list[0] + "_" + chr(textualMemoryCount) + "')."
		namedIndividualList.append(namedIndividual)
		classAssertion = "classAssertion('" + prefix + "TextureMemory','" + prefix + processor + list[0] + "_" + chr(textualMemoryCount) + "')."
		classAssertionList.append(classAssertion)
		list[0] = processor + list[0] + "_" + chr(textualMemoryCount)
		textualMemoryCount = textualMemoryCount + 1
		
	propertyAssertion = "propertyAssertion('" + prefix + "consistsOf','" + prefix + processor + "','" + prefix + list[0] + "')."
        propertyAssertionList.append(propertyAssertion)

	i = i + 1
	propertyAssertion = "propertyAssertion('" + prefix + "hasID','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
	propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i] == "Y"):
		propertyAssertion = "propertyAssertion('" + prefix + "softwareManageable','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#boolean','" + "true" + "')))."
		propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "N"):
		propertyAssertion = "propertyAssertion('" + prefix + "softwareManageable','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#boolean','" + "false" + "')))."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i] == "rw"):
		propertyAssertion = "propertyAssertion('" + prefix + "accessible','" + prefix + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "r"):
		propertyAssertion = "propertyAssertion('" + prefix + "accessible','" + prefix + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "w"):
		propertyAssertion = "propertyAssertion('" + prefix + "accessible','" + prefix + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('" + prefix + "hasDimension','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
        	propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
		propertyAssertion = "propertyAssertion('" + prefix + "hasSizeValue','" + prefix + list[0] + "',literal('" + list[i] + "'))."
		propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		i = i + 1
		if(list[i][-1] == '>'):
			propertyAssertion = "propertyAssertion('" + prefix + "hasSizeValue','" + prefix + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                	propertyAssertionList.append(propertyAssertion)
		elif(1):
			i = i + 1
			propertyAssertion = "propertyAssertion('" + prefix + "hasSizeValue','" + prefix + list[0] + "',literal('" + list[i-2] + " " + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
                propertyAssertion = "propertyAssertion('" + prefix + "hasBlockSizeValue','" + prefix + list[0] + "',literal('" + list[i] + "'))."
                propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
                i = i + 1
                if(list[i][-1] == '>'):
                        propertyAssertion = "propertyAssertion('" + prefix + "hasBlockSizeValue','" + prefix + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
                elif(1):
                        i = i + 1
                        propertyAssertion = "propertyAssertion('" + prefix + "hasBlockSizeValue','" + prefix + list[0] + "',literal('" + list[i-2] + " " + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('" + prefix + "threadsGroup','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		propertyAssertion = "propertyAssertion('" + prefix + "threadsGroup','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i].isdigit()):
                propertyAssertion = "propertyAssertion('" + prefix + "banks','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
                propertyAssertion = "propertyAssertion('" + prefix + "hasLatencyValue','" + prefix + list[0] + "',literal('" + list[i] + "'))."
                propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
                i = i + 1
                if(list[i][-1] == '>'):
                        propertyAssertion = "propertyAssertion('" + prefix + "hasBlockSizeValue','" + prefix + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i][0] == '<' and list[i][-1] == '>'):
		if(list[i][1] != '>'):
			propertyAssertion = "propertyAssertion('" + prefix + "hasUpperLevel','" + prefix + list[0] + "','" + prefix + list[i][1:len(list[i])-1] + "')."
                        propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		origin = list[0]
		while(1):
			if(list[i][-1] == '>'): break
			if(list[i][0] == '<'):
				propertyAssertion = "propertyAssertion('" + prefix + "hasUpperLevel','" + prefix + list[0] + "','" + prefix + list[i][1:len(list[i])] + "')."
				propertyAssertionList.append(propertyAssertion)
				origin = list[i][1:len(list[i])]
			elif(1):
				propertyAssertion = "propertyAssertion('" + prefix + "hasUpperLevel','" + prefix + origin + "','" + prefix + list[i] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i]
			i = i + 1
		propertyAssertion = "propertyAssertion('" + prefix + "hasUpperLevel','" + prefix + origin + "','" + prefix + list[i][0:len(list[i])-1] + "')."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] == '<' and list[i][-1] == '>'):
               	if(list[i][1] != '>'):
                       	propertyAssertion = "propertyAssertion('" + prefix + "hasLowerLevel','" + prefix + list[0] + "','" + prefix + list[i][1:len(list[i])-1] + "')."
                       	propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
             	origin = list[0]
                while(1):
                        if(list[i][-1] == '>'): break
                        if(list[i][0] == '<'):
                                propertyAssertion = "propertyAssertion('" + prefix + "hasLowerLevel','" + prefix + list[0] + "','" + prefix + list[i][1:len(list[i])] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i][1:len(list[i])]
                        elif(1):
                                propertyAssertion = "propertyAssertion('" + prefix + "hasLowerLevel','" + prefix + origin + "','" + prefix + list[i] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i]
                        i = i + 1
                propertyAssertion = "propertyAssertion('" + prefix + "hasLowerLevel','" + prefix + origin + "','" + prefix + list[i][0:len(list[i])-1] + "')."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1
	
	if(list[i] == "core" or list[i] == "sm" or list[i] == "tpc" or list[i] == "die"):
		propertyAssertion = "propertyAssertion('" + prefix + "shareScope','" + prefix + list[0] + "','" + prefix + list[i] + "')."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('" + prefix + "pieces','" + prefix + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i][0] == '<'):
		i = i + 1
		propertyAssertion = "propertyAssertion('" + prefix + "concurrencyFactor','" + prefix + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                propertyAssertionList.append(propertyAssertion)
	i = i + 1

# everything else is serial condition
	

for namedIndividual in namedIndividualList:
	output.write(namedIndividual+'\n')
for propertyAssertion in propertyAssertionList:
	output.write(propertyAssertion+'\n')
for classAssertion in classAssertionList:
	output.write(classAssertion+'\n')

input.close()
output.close()
