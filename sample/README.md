### Compile

	nvcc prog1.cu
	nvcc prog2.cu

	gcc -o a prog1.c
	gcc -o a prog2.c

### Run

	./a.out
	./a

### Output

The first line of the output is the time in microsecond used to execute the "kernel" function

The following lines of the output is the elements of C[i]

### Description

Develop a CUDA program that uses GPU to achieve the following:

C[B[i]] = A[i];

Where, A, B, C are three arrays with N elements contained in each. The values in B[i] are between 0 and N-1. Elements in A and B arrays are generated at the beginning of your program (CPU part of the code). Try the following two cases:

1. B[i] = i;
2. B[i] contains some random number in the valid range.
