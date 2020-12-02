import heapq

lists = [[4,2,6,8,1,3], [6,3,1,19,17]]
sorted_lists = []
for each in lists:
    sorted_lists.append(sorted(each))

def merged(lists):
    heap = []
    final_list = []
    for i, j in enumerate(lists):
        heap.append((j[0], i, 0))    
    heapq.heapify(heap)

    while heap:
        val, list_ind, ele_ind = heapq.heappop(heap)
        final_list.append(val)
        if ele_ind + 1 < len(lists[list_ind]):
            next_tup = (lists[list_ind][ele_ind + 1],
                          list_ind,
                          ele_ind + 1)
            heapq.heappush(heap, next_tup)
    return final_list

print(merged(sorted_lists))