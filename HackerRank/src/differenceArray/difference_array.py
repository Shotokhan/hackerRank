def manipulation(n, queries):
    l = [0]*(n+1)
    m = x = 0
    for query in queries:
        l[query[0] - 1] = l[query[0] - 1] + query[2]
        l[query[1]] = l[query[1]] - query[2]
    for i in l:
        x = x + i
        if x > m:
            m = x
    return m