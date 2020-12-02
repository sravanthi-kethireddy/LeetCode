def findTriplets(arr): 
    found = False
    n = len(arr)
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found") 
# findTriplets([0, -1, 2, -3, 1]) 

def subarraySum(nums, k):
        from collections import defaultdict
        sums = defaultdict(int)
        result = 0
        current_sum = 0
        for n in nums:
            current_sum += n
            if current_sum == k:
                result += 1
                
            diff = current_sum - k
            if diff in sums:
                result += sums[diff]
            sums[current_sum] += 1
        return result
# print(subarraySum([1,3,-1,5,4,5,-1],4))

def subarray_zero(arr):
    from collections import defaultdict
    maxLength = 0
    currentSum = 0
    myDict = defaultdict(int)

    for i in range(len(arr)):
        if arr[i] == 0 and maxLength == 0:
            maxLength=1
        if currentSum == 0:
            maxLength=i+1
        currentSum +=arr[i]
        if currentSum in myDict:
            maxLength = max(i-myDict[currentSum], maxLength)
        else:
            myDict[currentSum] = i 
    return maxLength
print(subarray_zero([15,-2,2,-8,1,7,10]))

