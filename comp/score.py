def score(lats, clats, reqs, sol):
    s = 0
    rs = 0
    for (v, e, r) in reqs:
        m = lats[e]
        for l, c in clats[e]:
            if((v in sol[c]) and (l < m)):
                m = l
        s += r*(lats[e] - m)
        rs += r
    return 1000*s/rs
