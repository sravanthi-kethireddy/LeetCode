def isValid(graph, color):
    colored_neighbors = []
    last_color= color[-1]
    last_vertex = len(color)-1
    for i, has_edge in enumerate(graph[last_vertex]):
        if has_edge and i < last_vertex:
            colored_neighbors.append(i)
    for each in colored_neighbors:
        if colored_neighbors[each]==last_color:
            return False
    return True

def colorable(graph, k, color=[]):
    if len(color)==len(graph):
        return True
    for i in range(k):
        color.append(i)
        if isValid(graph, color):
            if colorable(graph, k, color):
                return True
        color.pop()
    return True

houses = {
  0: [1,2],
  1: [0,2,3,4],
  2: [1],
  3: [1, 2],
  4: [0]

}

# print(colorable(houses, 2))
# exit()
houses = {
  0: [1,2],
  1: [0,2,3,4],
  2: [1],
  3: [1, 2],
  4: [0]

}
def valid(graph, colors):

    last_vertex = len(colors) - 1
    last_color = colors[-1]

    colored_neighbors = [x for x in graph[last_vertex] if x < last_vertex]

    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False
    return True

def colorable2(graph, k, colors=[]):

    if len(colors) == len(graph):
        return True

    for i in range(k):
        colors.append(i)
        if valid(graph, colors):
            if colorable2(graph, k, colors):
              return True, colors
        colors.pop()

    return False

# print(colorable2(houses, 2))


def isBiparteBFS(graph):
    seen = {}
    for i in range(len(graph)):
        if i not in seen:
            if checkBFS(graph, i, seen) == False:
                return False
    return True

def checkBFS(graph, start, seen):
    q = [(start, 1)]
    while len(q)>0:
        pop, color = q.pop(0)
        if pop in seen:
            if seen[pop] != color:
                return False
            continue
        seen[pop] = color
        vertices = graph[pop]
        for v in vertices:
            q.append((v, -color))
    return False

isBiparteBFS([[1,3], [0,2], [1,3], [0,2]])
def isBipartiteDFS( graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    seen = {}
    # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
    for i in range(len(graph)):
        if i not in seen:
            if checkDFS(graph, i, 1, seen) == False:
                return False
    return True

def checkDFS(graph, node, color, seen):
    if node in seen:
        if seen[node] != color:
            return False
        return True
    seen[node] = color
    vertices = graph[node]
    for v in vertices:
        if checkDFS(graph, v, -color, seen) == False:
            return False
    return True