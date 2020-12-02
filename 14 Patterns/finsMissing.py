def findMissing(l):
    n = len(l)+1
    sumN = n*(n+1)/2
    print(sumN)
    print(sum(l))
    print(sumN - sum(l))
def fimdMissing2(l):
    
    for each in range(1,len(l)):
        if l[each] - l[each-1] != 1:
            print (int((l[each] + l[each-1])/2))


# findMissing([1,2,4,5,6,7,8])
fimdMissing2([1,2,4,5,6,7,9])
            #   0 1 2 3 4 5 6
def strstr(haystack, needle):
    if not needle:
        return 0
    # if 
    return(haystack.find(needle))


haystack = "hello"
needle = ""
print(strstr(haystack, needle))
