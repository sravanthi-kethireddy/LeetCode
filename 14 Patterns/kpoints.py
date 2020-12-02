import math
def distance(point):
        return (math.sqrt(pow(point[0],2) + pow(point[1], 2)))

def kpoints(points, n):
    dist = []
    for each in points:
        dist.append((each, distance(each)))
    
    dist = sorted(dist, key= lambda x: x[1])
    ans = []
    for each in dist[:n]:
        ans.append(each[0])
    print (ans)

    
kpoints([[3,3],[5,-1],[-2,4]], 2)