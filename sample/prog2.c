#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
vector(int *A, int *B, int *C, int numElements)
{
    int i;
    for(i = 0; i < numElements; i ++)
    {
        C[B[i]] = A[i];
    }
}

int main(int argc, char **argv)
{
    struct timeval start, end;
    int i;
    int numElements = 5000000;
    size_t size = numElements * sizeof(int);

    int *h_A = (int *)malloc(size);
    int *h_B = (int *)malloc(size);
    int *h_C = (int *)malloc(size);
    if (h_A == NULL || h_B == NULL || h_C == NULL) fprintf(stderr, "Failed to allocate host vectors!\n");

    // Initialize the host input vectors
    for (i = 0; i < numElements; i++)
    {
        h_A[i] = i;
        h_B[i] = rand()%numElements;
    }
    gettimeofday(&start, NULL);
    vector(h_A, h_B, h_C, numElements);
    gettimeofday(&end, NULL);
    printf("%ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
		  - (start.tv_sec * 1000000 + start.tv_usec)));
    for(i = 0; i < numElements; i ++) printf("C[%d] = %d.\n",i,h_C[i]);
    free(h_A);
    free(h_B);
    free(h_C);
}

