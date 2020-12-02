class Solution:
    def cmp_to_key(self,mycmp):
        class K(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0
        return K
    def mycmp(self, a, b):
        if a+b > b+a:
            return -1
        else:
            return 1
        #  return 0
    def largestNumber(self, nums):
        ans = ''.join(sorted(map(str,nums), key=self.cmp_to_key(self.mycmp)))
        if ans[0] == '0':
            return 0
        else:
            return ans
    def multiply(self, num1, num2):
        n, m = len(num1), len(num2)
        if not n or not m:
            return "0"
        
        result = [0] * (n + m)
        print(result)
        for i in reversed(range(n)):
            print('->', i)
            for j in reversed(range(m)):
                print('-->', j)
                current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j])
                result[i + j + 1] = current % 10
                result[i + j] += current // 10
        
        for i, c in enumerate(result):
            if c != 0:
                return "".join(map(str, result[i:]))
        
        return "0"

obj1 = Solution()
# print(obj1.largestNumber([0,10,1]))
print(obj1.multiply("123","456"))
    

def num_excel(num):
    ans = ''
    if num <=26:
        return(chr(num))
    while num !=0:
        num, firstChar = divmod(num, 26)
        ans+=chr(64+firstChar)
    return(ans[::-1])
# print(num_excel(53))

# largest_num([3,30,34,5,9])
# largest_num([87,9])