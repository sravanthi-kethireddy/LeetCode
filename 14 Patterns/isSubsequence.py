def isSubsequence(s,t):
    ans = []
    for i in t:
        for j in s:
            if i == j:
                ans.append(j)
    ans = ''.join(x for x in ans)
    if ans == s:
        return True
    return False

print(isSubsequence("gksrek","geeksforgeeks"))