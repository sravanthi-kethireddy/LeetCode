import collections

def canFinish(numCourses, prerequisites):
    forward = {i: set() for i in range(numCourses)}
    # print(forward)
    backward = collections.defaultdict(set)
    # print(backward)
    for i, j in prerequisites:
        print(i,j)
        forward[i].add(j)
        backward[j].add(i)
    # print(forward)
    # print(backward)
    #nodes without incoming edges
    stack = [node for node in range(numCourses) if not backward[node]]
    # print(stack)
    while stack:
        node = stack.pop()
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                stack.append(neigh)
        backward.pop(node)
    # print(backward)
    return not backward
print(canFinish(4, [[1,0], [2,3]]))
# print (canFinish(5, [[1,0],[0,1],[0,2],[2,3],[3,4],[2,0]]))

