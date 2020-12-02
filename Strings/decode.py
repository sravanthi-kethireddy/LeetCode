def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    intStack = []
    alphaStack = []
    ans = ''
    if not s:
        return ''
    for each in s:
        if each.isdigit():
            intStack.append(each)
        if each.isalpha() or each == '[':
            alphaStack.append(each)
        if each == ']':
            popVal = ''
            subStr = ''
            intVal = intStack.pop()
            while popVal != '[':
                # print(alphaStack)
                subStr += popVal
                popVal = alphaStack.pop()
            joinedStr = int(intVal)*subStr[::-1]
            alphaStack.append(joinedStr)
            # print(alphaStack)
        print(alphaStack)
    

        
s = "3[a]2[bc]"
decodeString(s)
s = "3[a2[c]]"
decodeString(s)
s = "2[abc]3[cd]ef"
decodeString(s)
