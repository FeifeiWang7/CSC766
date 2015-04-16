import sys
input = open(sys.argv[1], 'r')
output = open("output.txt", 'w')

namedIndividualList = []
propertyAssertionList = []

while 1:
	i = 0
	line = input.readline()
	if not line: break
	list = line.split(' ')
	
	namedIndividual = "namedIndividual('" + list[0] + "')."
	namedIndividualList.append(namedIndividual)
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

input.close()
output.close()
