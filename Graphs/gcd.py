def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    itr = max(arr)
    val = False
    while itr>0:
        itr_lst = [x%itr for x in arr]
        cheeck = (all(v == 0 for v in itr_lst))
        
        if cheeck == True:
            return itr
        itr -= 1
        
    pass

print(generalizedGCD(5,[2,4,6]))