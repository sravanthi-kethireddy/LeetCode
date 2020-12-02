def spin_words(sentence):
    # Your code goes here
       
    sen = sentence.split(" ")
    for (i,each) in enumerate(sen):
        print(i,each)
        if len(each)>=5:
            sen[i] = each[::-1]
        else:
            sen[i] = each
        
    return " ".join(x for x in sen)

# print(spin_words("welcome to the jungle"))

def array_diff(a, b):
    #your code here
    for val in b:
        a = list(filter(lambda x: x != val, a))
    print(a)

# array_diff([],[2])

import math
def narcissistic( value ):
    # Code away
    digitSum = [math.pow(int(i),3) for i in str(value)]
    # print(ans)
    # for i in str(value):
    #     i = int(i)
    #     sum += math.pow(i,3)
    if sum(digitSum) == value:
        return (str(value)+' is narcissistic')
    else:
        return (str(value)+' is not narcissistic')
import string
# print(narcissistic(4887))
def alphabet_position(text):
    ans = ''
#     for alphabet in text:
#         if alphabet.isalpha():
#             ans += str(ord(alphabet.lower()) - 96) + ' '
# #         elif int(alphabet) > 0:
# #             ans += str(alphabet) + ' '
#     lst = text.split(" ")
#     lst.pop()
#     for each in lst:
#     	if int(each) > 0:
#     		ans += each + ' '
#     return ans
#     pass
    alphabet = string.ascii_lowercase
    for each in text:
        # print (each)
        if each in alphabet:
            ans += str(ord(each.lower()) - 96) + ' '
        
    return ans
    # return ' '.join([str(ord(char)-96) if char in alphabet else char for char in text])

def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) == 10:
        lat = ['w','e']
        lon = ['n', 's']
        dirWeights = {'n':1, 's':-1, 'w':-1, 'e':1}
        lateral = 0 
        longitudinal = 0
        for each in walk:
            if each in lat:
                lateral += dirWeights[each]
            if each in lon:
                longitudinal += dirWeights[each]
        print(lateral, longitudinal)
        if lateral == 0 and longitudinal ==0:
            return True
        
    return False
    
# print(alphabet_position('-41 -46 -47 -45 -44 -47 -46 -39 -43 -46 '))
# print(alphabet_position('sravanthi kethireddy'))
# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
