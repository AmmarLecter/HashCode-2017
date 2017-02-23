#!/usr/bin/env python

import heapq

import sys

from simann import simann
from score import score

V = E = R = C = X = 0

def read_line():
    return [int(i) for i in raw_input().split()]

def parse():
    global V, E, R, C, X
    V, E, R, C, X = read_line()
    latencies = [0] * E
    cache_latencies = [{} for _ in xrange(E)]
    requests = []
    sizes = read_line()
    for i in xrange(E):
        l, K = read_line()
        latencies[i] = l
        for j in xrange(K):
            c, L = read_line()
            cache_latencies[i][c] = L
    for _ in xrange(R):
        v, e, n = read_line()
        requests.append((v, e, n))
    return sizes, latencies, cache_latencies, requests


def out(cached):
    print len(cached)
    for idx, server in enumerate(cached):
        print idx,
        print ' '.join(map(str, server))

def main():
    sizes, latencies, cache_latencies, requests = parse()
    servers = simann(V, E, R, C, X, sizes, latencies, cache_latencies, requests)
    out(servers)
    print >> sys.stderr, score(latencies, cache_latencies, requests, servers)

if __name__ == "__main__": main()
