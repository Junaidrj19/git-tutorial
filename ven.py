def filter_list(l):
    p = [x for x in l if isinstance(x,int)]
    return p

print(filter_list([1,2,'a',123,'123']))
