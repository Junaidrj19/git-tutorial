def dig_pow(n,p):
    digits = [int(x) for x in str(n)]
    total = sum(d**(p+i) for i,d in enumerate(digits))
    return total//n if total%n==0 else -1

print(dig_pow(46288,3))
