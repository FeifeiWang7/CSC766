## Ontology-Based Data Placement Optimizations for GPU

Extending an existing ontology-based program analysis tool to provide guidance on data placement on GPU, including

* a tool to convert MSL specifications into ontology
* a tool to convert Data Access Patterns into ontology

#### Structure of the code
There are two tools. One tool can convert MSL specifications into ontology. The other tool can convert Data Access Patterns used by PORPLE into ontology.

##### Structure of the MSL tool
If you are in the Ontology directory, open the code by:

	cd MSL_To_Ontology
	vim my_parser.py

The first part of the code is to generate some general information about ontology such as the GPU type, and put them in a list.

The second part of the code is to generate ontology information about the processor, and put them in a list. For example, the number of SMs per TPC.

The third part of the code is to generate ontology information about the memory systems, and put them in a list. For example, globalMem.

The last part of the code is to print the lists we generated to a file called output.txt.
 
##### Structure of the data access patterns tool 
The data access patterns tool is very simple. It just extracts the name of the memory as namedIndividuals, and assigns them total memory access time, L1 cache hit, L2 cache hit, and off-chip memory access time. 

#### Installation and Execution
All one need to install is Python 2.7

	sudo apt-get install build-essential
	sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

	wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
	tar -xvf Python-2.7.5.tgz
	cd Python-2.7.5

	./configure
	make
	sudo make install

After installing Python 2.7, run the tools with the testcases called input.txt
	
	cd MSL_To_Ontology
	python my_parser.py input.txt 

	cd ..
	cd DAP_To_Ontology
	python my_parser.py input.txt 

#### Output
The output is stored in files called output.txt under the MSL_To_Ontology and DAP_To_Ontology directories. output.txt includes 

* namedIndividual
* propertyAssertion
* classAssertion

For example, namedIndividual('M2075globalMem') means that M2075globalMem is a particular kind of memory system. It can be used in propertyAssertion and classAssertion.

There are many propertyAssertions. I cannot explain all of them. So I just list a few properties here as an example of how to illustrate the ouput.
 
propertyAssertion('consistsOf','M2075','M2075globalMem') means that M2075globalMem is consisted of by M2075.

propertyAssertion('hasID','M2075globalMem',literal(type('http://www.w3.org/2001/XMLSchema#integer','8'))) means that M2075globalMem has an ID which is 8.

propertyAssertion('softwareManageable','M2075globalMem',literal(type('http://www.w3.org/2001/XMLSchema#boolean','true'))) means that M2075globalMem is software manageable.

propertyAssertion('accessible','M2075globalMem',literal(rw)) means that M2075globalMem has read and write access.

propertyAssertion('threadsGroup','M2075globalMem',literal(type('http://www.w3.org/2001/XMLSchema#integer','32'))) means that M2075globalMem has threadGroup of 32.

propertyAssertion('hasLatencyValue','M2075globalMem',literal('600clk')) means the latency value of M2075globalMem is 600clk.

propertyAssertion('hasUpperLevel','M2075globalMem','L2') means that M2075globalMem has an upper level that is L2.

In the end, classAssertion('GlobalMemory','M2075globalMem') means that M2075globalMem is a kind of GlobalMemory.

#### Limitation
The lilmitation of the code is that it requires the syntax to be correct in the input files. If there are syntax errors in the input files, it cannot detect the errors.
