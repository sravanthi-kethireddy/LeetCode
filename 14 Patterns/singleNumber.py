from collections import Counter
class Solution:
    def singleNumber(self, nums):
        myDict = Counter(nums)
        print(myDict)
        for (key, value) in myDict.items():
            print (key, value)
            if value == 1:
                return key
            

obj = Solution()
print(obj.singleNumber([0,1,0,1,0,1,99]))