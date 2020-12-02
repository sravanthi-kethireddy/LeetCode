from collections import defaultdict
def charDict(word):
    myDict = {}
    for each in word:
        if each in myDict:
            myDict[each] += 1
        else:
            myDict[each] = 1
    return myDict

def possible_words(words, charSet):
    for each in words:
        flag = 1
        myDict = charDict(each)
        # print(myDict)
        for key in myDict:
            # print (key)
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != myDict[key]:
                    flag = 0
        if flag == 1:
            print(each)


  
words = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run'] 
charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l'] 
possible_words(words, charSet) 

def wordBreak(s, wordDict):
    if not s:
        return False
    queue = [0]
    while queue:
        start = queue.pop(0)
        if start == len(s):
            return True
        for word in wordDict:
            if s[start:].startswith(word):
                end = start + len(word)
                if end not in queue:
                    queue.append(end)
    return False




# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# print(wordBreak(s, wordDict))


def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True

    for i, word in enumerate(words):
        reduce(dict.__getitem__, word, trie)[END] = i

    stack = trie.values()
    ans = ""
    while stack:
        cur = stack.pop()
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans