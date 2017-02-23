def score(lats, clats, reqs, sol):
    s = 0
    for (v, e, r) in reqs:
        m = 1001
        for c, l in clats[e].iteritems():
            if((v in sol[c]) and (l < m)):
                m = l
        s += r*(lats[e] - m)
    return s
