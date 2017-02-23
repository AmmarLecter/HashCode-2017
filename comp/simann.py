import fileinput

from random import randint, random
from score import score

def simann(firstsol, V, E, R, C, X, sizes, latencies, cache_latencies, requests):
    Y = 10
    N = 1000
    best_score = 0
    best_sol = [set() for x in range(C)]

    def cache_size(cacheid):
        return sum([v for v in sizes if v in caches[cacheid]])

    def find_cache(videoid):
        for i, x in enumerate(caches):
            if videoid in x:
                return i

        return -1

    def remove_from_cache(videoid):
        idx = find_cache(videoid)
        if idx >= 0:
            caches[idx].remove(videoid)

    def move_to_cache(videoid, cacheid):
        size = cache_size(cacheid)
        
        if sizes[videoid] + size > X:
            return False
        else:
            remove_from_cache(videoid)
            caches[cacheid].add(videoid)
            return True

    for i in range(Y):
        caches = [set() for x in firstsol]
        for j in range(N):
            prevsol = [set(x) for x in caches]

            rv = randint(0, V-1)
            rc = randint(0, C-1)

            move_to_cache(rv, rc)

            curr_score = score(latencies, cache_latencies, requests, caches)

            if curr_score > best_score:
                best_sol = [set(x) for x in caches]
            else:
                if random() < (float(j) / float(N)):
                    caches = prevsol

    return best_sol 
