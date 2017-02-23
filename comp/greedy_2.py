import heapq

def greedy(E, C, X, sizes, latencies, cache_latencies, requests):
    # Initializations
    heap = []
    available = [X] * C
    servers = [set() for _ in xrange(C)]
    endpoint_requests = [[] for _ in xrange(E)]
    sum_requests = [0] * E
    # Parsing requests
    for r in requests:
        v, e, n = r
        endpoint_requests[e].append((n, v, e))
        heapq.heappush(heap, (n, e, v))
    for i in xrange(len(endpoint_requests)):
        endpoint_requests[i].sort()
    req = sorted(endpoint_requests, key=lambda x: sum(i[0] for i in x))
    for req_list in req:
        for r in req_list:
            n, v, e = r
            size = sizes[v]
            for latency, cache_server in cache_latencies[e]:
                if v in servers[cache_server]:
                    break
                if available[cache_server] >= size:
                    available[cache_server] -= size
                    servers[cache_server].add(v)
                    break
    return servers
