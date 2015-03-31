#include <stdio.h>
#include <cuda_runtime.h>
#include <time.h>
#include <sys/time.h>

__global__ void
vector(int *A, int *B, int *C, int numElements)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < numElements)
    {
        C[B[i]] = A[i];
    }
}

int main(int argc, char **argv)
{
    struct timeval start, end;
    cudaError_t err = cudaSuccess;

    int numElements = 5000000;
    size_t size = numElements * sizeof(int);

    int *h_A = (int *)malloc(size);
    int *h_B = (int *)malloc(size);
    int *h_C = (int *)malloc(size);
    if (h_A == NULL || h_B == NULL || h_C == NULL) fprintf(stderr, "Failed to allocate host vectors!\n");

    // Initialize the host input vectors
    srand(time(NULL));
    for (int i = 0; i < numElements; i++)
    {
        h_A[i] = i;
        h_B[i] = rand()%numElements;
    }

    // Allocate the device input vector A
    int *d_A = NULL;
    err = cudaMalloc((void **)&d_A, size);
    if (err != cudaSuccess) fprintf(stderr, "Failed to allocate device vector A (error code %s)!\n", cudaGetErrorString(err));

    // Allocate the device input vector B
    int *d_B = NULL;
    err = cudaMalloc((void **)&d_B, size);
    if (err != cudaSuccess) fprintf(stderr, "Failed to allocate device vector B (error code %s)!\n", cudaGetErrorString(err));

    // Allocate the device output vector C
    int *d_C = NULL;
    err = cudaMalloc((void **)&d_C, size);
    if (err != cudaSuccess) fprintf(stderr, "Failed to allocate device vector C (error code %s)!\n", cudaGetErrorString(err));

    // Copy the host input vectors A and B in host memory to the device input vectors in device memory
    err = cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    if (err != cudaSuccess) fprintf(stderr, "Failed to copy vector A from host to device (error code %s)!\n", cudaGetErrorString(err));
    err = cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
    if (err != cudaSuccess) fprintf(stderr, "Failed to copy vector B from host to device (error code %s)!\n", cudaGetErrorString(err));

    // Launch the Vector Add CUDA Kernel
    int threadsPerBlock = 512;
    int blocksPerGrid =(numElements + threadsPerBlock - 1) / threadsPerBlock;
 //   printf("CUDA kernel launch with %d blocks of %d threads\n", blocksPerGrid, threadsPerBlock);
    
    gettimeofday(&start, NULL);
    vector<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, numElements);
    gettimeofday(&end, NULL);
    printf("%ld\n", ((end.tv_sec * 1000000 + end.tv_usec)
		  - (start.tv_sec * 1000000 + start.tv_usec)));
    err = cudaGetLastError();
    if (err != cudaSuccess) fprintf(stderr, "Failed to launch vectorAdd kernel (error code %s)!\n", cudaGetErrorString(err));

    // Copy the device result vector in device memory to the host result vector in host memory.
 //   printf("Copy output data from the CUDA device to the host memory\n");
    err = cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
    if (err != cudaSuccess) fprintf(stderr, "Failed to copy vector C from device to host (error code %s)!\n", cudaGetErrorString(err));

    // Verify that the result vector is correct
   for (int i = 0; i < numElements; i++) fprintf(stderr, "Element in C[%d] is %d!\n", i, h_C[i]);

    // Free device global memory
    err = cudaFree(d_A);
    if (err != cudaSuccess) fprintf(stderr, "Failed to free device vector A (error code %s)!\n", cudaGetErrorString(err));
    err = cudaFree(d_B);
    if (err != cudaSuccess) fprintf(stderr, "Failed to free device vector B (error code %s)!\n", cudaGetErrorString(err));
    err = cudaFree(d_C);
    if (err != cudaSuccess) fprintf(stderr, "Failed to free device vector C (error code %s)!\n", cudaGetErrorString(err));

    // Free host memory
    free(h_A);
    free(h_B);
    free(h_C);

    // Reset the device and exit
    err = cudaDeviceReset();
    if (err != cudaSuccess) fprintf(stderr, "Failed to deinitialize the device! error = %s\n", cudaGetErrorString(err));
}

