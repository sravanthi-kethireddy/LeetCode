def simplifyPath(path):
    splitted = [token for token in path.split("/") if token]
    # print(splitted)
    
    stack = []
            
    for token in splitted:
        if token == "..": stack.pop() if stack else None
        elif token != ".": stack.append(token)
    print(stack)
    return "".join(["/", "/".join(stack)])

def removeRepeats(string):
    output = ''
    for each in string:
        if each not in output:
            output += each
    return output

def reorderLogs(logs):
    alphaLog = []
    digitLog = []
    
    for log in logs:
        if log.split()[1].isdigit():
            digitLog.append(log)
        if log.split()[1].isalpha():
            alphaLog.append(log)
    print(alphaLog)
    alphaLog.sort(key=lambda log: log.split()[0])
    alphaLog.sort(key=lambda log: log.split()[1:])
    return alphaLog+digitLog
    # print(alphaLog)
        

print(reorderLogs(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
# print(removeRepeats("cddecoweubfskadaa"))
# print(simplifyPath("/a/../../b/../c//.//"))
# print(simplifyPath("/a//b////c/d//././/.."))
# print(simplifyPath("/home/"))