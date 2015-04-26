import sys
input = open(sys.argv[1], 'r')
output = open("output.txt", 'w')

prefix = "#"

namedIndividualList = []
propertyAssertionList = []
classAssertionList = []

processor = "M2075"
namedIndividualList.append("namedIndividual('" + processor + "').")
namedIndividualList.append("namedIndividual('" + processor + "Processor').")
propertyAssertion = "propertyAssertion('consistsOf','" + processor + "','" + processor + "Processor')."
propertyAssertionList.append(propertyAssertion)

classAssertion = "classAssertion('Tesla','"+ processor + "')."
classAssertionList.append(classAssertion)
classAssertion = "classAssertion('Processor','" + processor + "Processor')."
classAssertionList.append(classAssertion)

while 1:
	i = 0
	line = input.readline()
	if not line: break
	list = line.split(' ')

	if(list[0] == "die"): 
		namedIndividualList.append("namedIndividual('block').")
                namedIndividualList.append("namedIndividual('core').")
                namedIndividualList.append("namedIndividual('die').")
                namedIndividualList.append("namedIndividual('grid').")
                namedIndividualList.append("namedIndividual('sm').")
                namedIndividualList.append("namedIndividual('tpc').")
                namedIndividualList.append("namedIndividual('warp').")

		propertyAssertion = "propertyAssertion('numberOfDiesValue','" + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + "1" + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('TPCPerDie','" + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[2] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('SMPerTPC','" + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[6] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('CoresPerSM','" + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[10] + "')))."
		propertyAssertionList.append(propertyAssertion)
		propertyAssertion = "propertyAssertion('membus','" + processor + "Processor',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[14] + "')))."
		propertyAssertionList.append(propertyAssertion)

		classAssertion = "classAssertion('scope','block')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','core')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','die')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','grid')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','sm')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','tpc')."
		classAssertionList.append(classAssertion)
		classAssertion = "classAssertion('scope','warp')."
		classAssertionList.append(classAssertion)
		
		continue

	if(list[0] == "globalMem"):
		classAssertion = "classAssertion('GlobalMemory','" + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "L1"):
		classAssertion = "classAssertion('Cache','" + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "L2"):
		classAssertion = "classAssertion('Cache','" + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "constantMem"):
		classAssertion = "classAssertion('ConstantMemory','" + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "cL1"):
		classAssertion = "classAssertion('L1_constant','" + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "cL2"):
		classAssertion = "classAssertion('L2_constant','" + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "readonlyMem"):
		classAssertion = "classAssertion('ReadOnlyMemory','" + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "sharedMem"):	
		classAssertion = "classAssertion('SharedMemory','" + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "tL1"):
		classAssertion = "classAssertion('L1_texture','" + list[0] + "')."
		classAssertionList.append(classAssertion)
	elif(list[0] == "textureMem"):	
		classAssertion = "classAssertion('TextureMemory','" + processor + list[0] + "')."
		classAssertionList.append(classAssertion)
		
	namedIndividual = "namedIndividual('" + list[0] + "')."
	namedIndividualList.append(namedIndividual)

	propertyAssertion = "propertyAssertion('consistsOf','" + processor + "','" + list[0] + "')."
        propertyAssertionList.append(propertyAssertion)

	i = i + 1
	propertyAssertion = "propertyAssertion('hasID','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
	propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i] == "Y"):
		propertyAssertion = "propertyAssertion('softwareManageable','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#boolean','" + "true" + "')))."
		propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "N"):
		propertyAssertion = "propertyAssertion('softwareManageable','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#boolean','" + "false" + "')))."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i] == "rw"):
		propertyAssertion = "propertyAssertion('accessible','" + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "r"):
		propertyAssertion = "propertyAssertion('accessible','" + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i] == "w"):
		propertyAssertion = "propertyAssertion('accessible','" + list[0] + "',literal(" + list[i] + "))."
                propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('hasDimension','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
        	propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
		propertyAssertion = "propertyAssertion('hasSizeValue','" + list[0] + "',literal('" + list[i] + "'))."
		propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		i = i + 1
		if(list[i][-1] == '>'):
			propertyAssertion = "propertyAssertion('hasSizeValue','" + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                	propertyAssertionList.append(propertyAssertion)
		elif(1):
			i = i + 1
			propertyAssertion = "propertyAssertion('hasSizeValue','" + list[0] + "',literal('" + list[i-2] + " " + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
                propertyAssertion = "propertyAssertion('hasBlockSizeValue','" + list[0] + "',literal('" + list[i] + "'))."
                propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
                i = i + 1
                if(list[i][-1] == '>'):
                        propertyAssertion = "propertyAssertion('hasBlockSizeValue','" + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
                elif(1):
                        i = i + 1
                        propertyAssertion = "propertyAssertion('hasBlockSizeValue','" + list[0] + "',literal('" + list[i-2] + " " + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('threadsGroup','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		propertyAssertion = "propertyAssertion('threadsGroup','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i].isdigit()):
                propertyAssertion = "propertyAssertion('banks','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] != '<' and list[i][0].isdigit()):
                propertyAssertion = "propertyAssertion('hasLatencyValue','" + list[0] + "',literal('" + list[i] + "'))."
                propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
                i = i + 1
                if(list[i][-1] == '>'):
                        propertyAssertion = "propertyAssertion('hasBlockSizeValue','" + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
                        propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i][0] == '<' and list[i][-1] == '>'):
		if(list[i][1] != '>'):
			propertyAssertion = "propertyAssertion('hasUpperLevel','" + list[0] + "','" + list[i][1:len(list[i])-1] + "')."
                        propertyAssertionList.append(propertyAssertion)
	elif(list[i][0] == '<'):
		origin = list[0]
		while(1):
			if(list[i][-1] == '>'): break
			if(list[i][0] == '<'):
				propertyAssertion = "propertyAssertion('hasUpperLevel','" + list[0] + "','" + list[i][1:len(list[i])] + "')."
				propertyAssertionList.append(propertyAssertion)
				origin = list[i][1:len(list[i])]
			elif(1):
				propertyAssertion = "propertyAssertion('hasUpperLevel','" + origin + "','" + list[i] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i]
			i = i + 1
		propertyAssertion = "propertyAssertion('hasUpperLevel','" + origin + "','" + list[i][0:len(list[i])-1] + "')."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i][0] == '<' and list[i][-1] == '>'):
               	if(list[i][1] != '>'):
                       	propertyAssertion = "propertyAssertion('hasLowerLevel','" + list[0] + "','" + list[i][1:len(list[i])-1] + "')."
                       	propertyAssertionList.append(propertyAssertion)
        elif(list[i][0] == '<'):
             	origin = list[0]
                while(1):
                        if(list[i][-1] == '>'): break
                        if(list[i][0] == '<'):
                                propertyAssertion = "propertyAssertion('hasLowerLevel','" + list[0] + "','" + list[i][1:len(list[i])] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i][1:len(list[i])]
                        elif(1):
                                propertyAssertion = "propertyAssertion('hasLowerLevel','" + origin + "','" + list[i] + "')."
                                propertyAssertionList.append(propertyAssertion)
                                origin = list[i]
                        i = i + 1
                propertyAssertion = "propertyAssertion('hasLowerLevel','" + origin + "','" + list[i][0:len(list[i])-1] + "')."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1
	
	if(list[i] == "core" or list[i] == "sm" or list[i] == "tpc" or list[i] == "die"):
		propertyAssertion = "propertyAssertion('shareScope','" + list[0] + "','" + list[i] + "')."
		propertyAssertionList.append(propertyAssertion)
	i = i + 1

	if(list[i].isdigit()):
		propertyAssertion = "propertyAssertion('pieces','" + list[0] + "',literal(type('http://www.w3.org/2001/XMLSchema#integer','" + list[i] + "')))."
                propertyAssertionList.append(propertyAssertion)
        i = i + 1

	if(list[i][0] == '<'):
		i = i + 1
		propertyAssertion = "propertyAssertion('concurrencyFactor','" + list[0] + "',literal('" + list[i-1] + " " + list[i] + "'))."
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
