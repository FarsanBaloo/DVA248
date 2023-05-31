from numba import jit
import numpy
import time


@jit(nopython=True)
def ijk(A, B):
    # EST Cache Misses: 62'500
    n = A.shape[0]
    p = B.shape[1]
    m = A.shape[1]
    assert m == B.shape[0]
    C = numpy.zeros((n,p), dtype=numpy.uint32)
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


@jit(nopython=True)
def slow(A, B):
    n = A.shape[0]
    p = B.shape[1]
    m = A.shape[1]
    assert m == B.shape[0]
    C = numpy.zeros((n,p), dtype=numpy.uint32)

    # Your solution goes here
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[k][j] += A[k][i] * B[i][j]

    return C


@jit(nopython=True)
def fast(A, B):
    n = A.shape[0]
    p = B.shape[1]
    m = A.shape[1]
    assert m == B.shape[0]
    C = numpy.zeros((n,p), dtype=numpy.uint32)

    # your solution goes here
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][k] += A[i][j] * B[j][k]
    return C


def testMatrixProductFunction(A,B,f):
    print(f"\nTesting : {f.__name__}(A,B)")
    tic = time.perf_counter()
    C = f(A,B)
    toc = time.perf_counter()
    print(f"Elapsed time: {toc-tic:0.3f} seconds")
    assert numpy.array_equal(C,numpy.matmul(A,B))


A = numpy.random.randint(10, size=(1000,1000), dtype=numpy.uint32)
print(f"A belongs to {A[0][0].__class__.__name__}^[{A.shape[0]}x{A.shape[1]}]")
B = numpy.random.randint(10, size=(1000,1000), dtype=numpy.uint32)
print(f"B belongs to {B[0][0].__class__.__name__}^[{B.shape[0]}x{B.shape[1]}]")
# print(A.flags)
# print(B.flags)

#testMatrixProductFunction(A,B,ijk)
testMatrixProductFunction(A,B,slow)
#testMatrixProductFunction(A,B,fast)