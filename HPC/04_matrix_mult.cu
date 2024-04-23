#include <stdio.h>
#include <stdlib.h>

// CUDA code to multiply matrices
__global__
void multiply(int* A, int* B, int* C, int size) {
    // Uses thread indices and block indices to compute each element
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < size && col < size) {
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += A[row * size + i] * B[i * size + col];
        }
        C[row * size + col] = sum;
    }
}

void initialize(int* matrix, int size) {
    for (int i = 0; i < size * size; i++) {
        matrix[i] = rand() % 10;
    }
}

void print(int* matrix, int size) {
    for (int row = 0; row < size; row++) {
        for (int col = 0; col < size; col++) {
            printf("%d ", matrix[row * size + col]);
        }
        printf("\n");
    }
    printf("\n");
}

int main() {
    int* A, * B, * C;

    int N = 2;
    int blockSize = 16;

    int matrixSize = N * N;
    size_t matrixBytes = matrixSize * sizeof(int);

    A = (int*)malloc(matrixBytes);
    B = (int*)malloc(matrixBytes);
    C = (int*)malloc(matrixBytes);

    initialize(A, N);
    initialize(B, N);
    printf("Matrix A: \n");
    print(A, N);

    printf("Matrix B: \n");
    print(B, N);

    int* X, * Y, * Z;
    // Allocate space
    cudaMalloc(&X, matrixBytes);
    cudaMalloc(&Y, matrixBytes);
    cudaMalloc(&Z, matrixBytes);

    // Copy values from A to X
    cudaMemcpy(X, A, matrixBytes, cudaMemcpyHostToDevice);

    // Copy values from A to X and B to Y
    cudaMemcpy(Y, B, matrixBytes, cudaMemcpyHostToDevice);

    // Threads per CTA dimension
    int THREADS = 2;

    // Blocks per grid dimension (assumes THREADS divides N evenly)
    int BLOCKS = N / THREADS;

    // Launch kernel
    dim3 threads(THREADS, THREADS);
    dim3 blocks(BLOCKS, BLOCKS);
    multiply<<<blocks, threads>>>(X, Y, Z, N);

    cudaMemcpy(C, Z, matrixBytes, cudaMemcpyDeviceToHost);
    printf("Multiplication of matrix A and B: \n");
    print(C, N);

    free(A);
    free(B);
    free(C);

    cudaFree(X);
    cudaFree(Y);
    cudaFree(Z);

    return 0;
}
