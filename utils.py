def longest_consec(strarr,k):
    combine = []
    if k > len(strarr) or k <= 0 :
        return None
    for i in range(len(strarr)-k+1):
        new = "".join(strarr[i:i+k])
        combine.append(new)
    return max(combine,key = len)

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"],  2))
