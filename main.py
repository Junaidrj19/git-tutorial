def dig_pow(n,p):
    y = str(n)
    origin = n
    n = [int(x) for x in y]
    total = sum(d**(p+i) for i,d in enumerate(n))
    for k in range(total):
        if origin * k == total:
            return k
    return -1
