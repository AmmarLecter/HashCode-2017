import fileinput

from random import randint, random
from score import score

def simann(firstsol, V, E, R, C, X, sizes, latencies, cache_latencies, requests):
    Y = 3
    N = 100
    best_score = score(latencies, cache_latencies, requests, firstsol)

    def cache_size(cache):
        return sum([v for v in sizes if v in cache])

    def find_cache(videoid):
        for i, x in enumerate(caches):
            if videoid in x:
                return i

        return -1

    def remove_from_cache(videoid):
        idx = find_cache(videoid)
        if idx >= 0:
            caches[idx].remove(videoid)
            l_sizes[idx] -= sizes[videoid]

    def move_to_cache(videoid, cacheid):
        size = l_sizes[cacheid]
        
        if sizes[videoid] + size > X:
            return False
        else:
            remove_from_cache(videoid)
            caches[cacheid].add(videoid)
            l_sizes[cacheid] += sizes[videoid]
            return True

    l_sizes = [cache_size(x) for x in firstsol]
    best_sol = [set(x) for x in firstsol]

    for i in range(Y):
        caches = [set(x) for x in firstsol]
        for j in range(N):
            prevsol = [set(x) for x in caches]

            rv = randint(0, V-1)

            for x in range(10):
                rc = randint(0, C-1)
                if move_to_cache(rv, rc):
                    break

            curr_score = score(latencies, cache_latencies, requests, caches)

            if curr_score > best_score:
                best_sol = [set(x) for x in caches]
                best_score = curr_score
            else:
                if random() < (float(j) / float(N)):
                    caches = prevsol

    return best_sol 
