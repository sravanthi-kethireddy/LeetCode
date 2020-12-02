def fibonacci(n):
    # ans = 1
    # for i in range(1,n+1):
    #     ans = ans*i
    # print("Brute force...")
    # print(ans)
    # print("Recursion...")
    if n == 0:
        return 0
    if n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def computeNth(n):
    prev, curr = 0,1 
    while n > 2:
        prev, curr = curr, curr+prev
        n-=1
    return curr

# print(fibonacci(10))
# print(computeNth(8))
# for i in range(10):
#     print(fibonacci(i))
# 0 1 1 2 3 5 8 13

def fib(n):
    first = 0
    second = 1
    fibList = [0,1]
    while n-2:
        nextVal = first+second
        first,second = second, nextVal
        fibList.append(nextVal)
        n = n-1
    print(fibList)
def fibRecur(n):
    print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)
# fibRecur(10)
def climbingStairs(n):
    val = n
    d = {1:1, 2:2}
    if n == 0:
        return 0
    if n == 1:
        return 1
    curr = 3
    while n:
        d[curr] = d[curr-1] + d[curr - 2]
        curr = curr + 1
        n = n-1
    print (d[val])
climbingStairs(4)
# 4 -> 1,1,1,1 | 2,2 | 1,2,1 |