import heapq

def greedy(sizes, latencies, cache_latencies, requests):
    # Initializations
    heap = []
    available = [X] * C
    servers = [set() for _ in xrange(C)]
    # Parsing requests
    for r in requests:
        v, e, n = r
        size = sizes[v]
        for cache_server, latency in cache_latencies[e].iteritems():
            heapq.heappush(heap, ((latencies[e] - latency) * n / size, e, cache_server, v))
    while(len(heap) > 0):
        _, endpoint, cache_server, video_id = heapq.heappop(heap)
        size = sizes[video_id]
        if any([video_id in servers[cs] for cs in cache_latencies[endpoint]]):
            continue
        if available[cache_server] >= size:
            available[cache_server] -= size
            servers[cache_server].add(video_id)
    return servers
