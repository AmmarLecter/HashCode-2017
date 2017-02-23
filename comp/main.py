#!/usr/bin/env python

V = E = R = C = X = 0

def read_line():
    return [int(i) for i in raw_input().split()]

def parse():
    V, E, R, C, X = read_line()
    latencies = [0] * E
    cache_latencies = [{} for _ in xrange(E)]
    requests = [{} for _ in xrange(E)]
    sizes = read_line()
    for i in xrange(E):
        l, K = read_line()
        latencies[i] = l
        for j in xrange(K):
            c, L = read_line()
            cache_latencies[i][c] = L
    for _ in xrange(R):
        v, e, n = read_line()
        requests[e][v] = n
    return sizes, latencies, cache_latencies, requests


def out(cached):
    for idx, server in enumerate(cached):
        print idx
        print ' '.join(map(str, server))

def greedy():
    pass

def main():
    sizes, latencies, cache_latencies, requests = parse()
    print sizes
    print latencies
    print cache_latencies
    print requests
    out()

if __name__ == "__main__": main()
