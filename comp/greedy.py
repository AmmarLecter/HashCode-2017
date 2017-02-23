import heapq

def greedy(C, X, sizes, latencies, cache_latencies, requests):
    # Initializations
    heap = []
    available = [X] * C
    servers = [set() for _ in xrange(C)]
    # Parsing requests
    for r in requests:
        v, e, n = r
        size = sizes[v]
        heapq.heappush(heap, (n, e, v))
    while(len(heap) > 0):
        _, endpoint, video_id = heapq.heappop(heap)
        size = sizes[video_id]
        for latency, cache_server in cache_latencies[endpoint]:
            if video_id in servers[cache_server]:
                break
            if available[cache_server] >= size:
                available[cache_server] -= size
                servers[cache_server].add(video_id)
                break
    return servers
