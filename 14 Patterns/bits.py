def countSetBits(n):
    count = 0
    while n:
        count+= n & 1 
        n >>=1
    return count
# Count number of bits to be flipped to convert A into B 
def flipped(a,b):
    return countSetBits(a ^ b)

def filp2tobe3(a,b,c):
    m = 1
    res = 0
    while a or b or c:
        ai, bi, ci = a&m, b&m, c&m
        res += (ai+bi) if ci == 0 else (ai+bi==0)
        a >>= 1
        b >>= 1
        c >>= 1
    return res

print(flipped(2,6))
print(filp2tobe3(8,3,5))