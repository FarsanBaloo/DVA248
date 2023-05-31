from numba import jit
import numpy
import time


@jit(nopython=True)
def OctantPopCount(points):
    assert points.shape[1] == 3
    counters = numpy.zeros(8, dtype=numpy.uint32)
    for p in points:
        if p[0]<0 and p[1]<0 and p[2]<0:
            counters[7] += 1
        elif p[0]<0 and p[1]<0 and not p[2]<0:
            counters[6] += 1
        elif p[0]<0 and not p[1]<0 and p[2]<0:
            counters[5] += 1
        elif p[0]<0 and not p[1]<0 and not p[2]<0:
            counters[4] += 1
        elif not p[0]<0 and p[1]<0 and p[2]<0:
            counters[3] += 1
        elif not p[0]<0 and p[1]<0 and not p[2]<0:
            counters[2] += 1
        elif not p[0]<0 and not p[1]<0 and p[2]<0:
            counters[1] += 1
        else:
            counters[0] += 1
    # print(counters)
    return counters


@jit(nopython=True)
def OctantPopCountNoIf(p):
    assert points.shape[1] == 3
    counters = numpy.zeros(8, dtype=numpy.uint32)
    # your solution goes here
    for i in p:
        counters[int(i[0]<0)*4 + int(i[1]<0) * 2 + int(i[2]<0)*1] += 1
    return counters


def testOctantPopCountFunction(points, f):
    print(f"\nTesting : {f.__name__}()")
    n = points.shape[0]
    tic = time.perf_counter()
    counters = f(points)
    toc = time.perf_counter()
    print(f"Elapsed time: {toc-tic:0.3f} seconds")
    return counters

points = numpy.random.random_sample((2000000, 3)) - 0.5
# print(points)
c1 = testOctantPopCountFunction(points, OctantPopCount)
c2 = testOctantPopCountFunction(points, OctantPopCountNoIf)

assert numpy.array_equal(c1,c2)