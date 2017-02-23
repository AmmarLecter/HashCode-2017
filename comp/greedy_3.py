import heapq

def greedy(w, E, C, X, sizes, latencies, cache_latencies, requests):
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
    new_lists = []
    for req_list in req:
        pososto = int(len(req_list)*w)
        to_process, rest = req_list[:pososto], req_list[pososto:]
        new_lists.append(rest)
        for r in to_process:
            n, v, e = r
            size = sizes[v]
            for latency, cache_server in cache_latencies[e]:
                if v in servers[cache_server]:
                    break
                if available[cache_server] >= size:
                    available[cache_server] -= size
                    servers[cache_server].add(v)
                    break

    for req_list in new_lists:
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
