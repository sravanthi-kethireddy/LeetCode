def maxSubArraywithK(arr, k):
    window = arr[:k]
    windowSumFirst = sum(window)
    
    for i in range(len(arr)):
        flag = 1
        window.append(arr[i])
        window = window[flag:]
        windowSum = sum(window)
        if windowSum > windowSumFirst:
            windowSumFirst = windowSum
        print(sum(window), window)
    print('-> max sub array', windowSumFirst)
        
def maxSubArray(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        print( max(arr[0], arr[1], sum(arr)))

    
    maxCurr = maxGlobal = arr[0]
    for each in range(1, len(arr)):
        # maxCurr = arr[each]
        maxCurr = max(arr[each], maxCurr + arr[each])
        # print (maxCurr)
        if maxCurr > maxGlobal:
            maxGlobal = maxCurr
    
            
    print(maxGlobal)


# xl

    

# maxSubArraywithK([90,1, 4, 2, 10, 90, 23, 3, 1, 0, 20, 90], 4)
# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# maxSubArray([-2, 1])
maxSubArray([1,-1,1])
