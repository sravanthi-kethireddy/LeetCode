def power(a,b):
	if b ==0:
		return 1
	res = 0
	ans = power(a, b-1)
	for i in range(a):
		res += ans
	return res
print(power(3,5))
exit()
def sqrtt(num):
	sqt = num / 2
	temp = 0
	while (sqt!=temp):
		temp = sqt
		sqt = (num/temp + temp)/2
	print (sqt)

sqrtt(3)
exit()
    			


def smallest_num(n):
	i = 0
	for i in range(1,n):
		if (i*i == n):
			return i
		else:
			small =  (i*i)
			if small > n:
				return (i-1, i)
arr = [1,4,7,9,11,16,17,18,19,20]
arr = [1,4,7,8,9,10]
arr = [1,4,7,9]
find = 16
def binary_search(arr, find):
	ans = False
	n = int(len(arr)/2)
	if n%2!=0:
		mid_ele = arr[n]
		print("->", arr, mid_ele)
		if mid_ele == find:
			ans =True

		if find > mid_ele:
			arr = arr[n+1:]

		if find < mid_ele:
			arr = arr[0:n]
		return (arr, ans)
	else:
		mid_ele = arr[n]
def binary_search_check(arr):
	i = len(arr)
	while i >= 0 and len(arr) >= 1:
		# print('#### ', binary_search(arr, find))
		arr,ans = binary_search(arr, find)
		if ans:
			break
		else:
			ans = False
		i -=1

	if ans:
		print("yay found it")
	else:
		print("life gave you lemons")

# binary_search(arr, 7)

def binary_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(n-i-1):
			if arr[j+1] < arr[j]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr

def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		minIdx = i
		for j in range(i+1,n):
			if arr[minIdx] > arr[j]:
				minIdx = j
		temp =arr[minIdx]
		arr[minIdx]=arr[i]
		arr[i]=temp
	return arr

def insertion_sort(arr):
	n = len(arr)
	i = 1
	while i < n:
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			temp = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = temp
			j-=1
		i +=1
	return arr
def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

def kadane(arr):
	max_curr = arr[0]
	max_global = arr[0]
	for i in range(1, len(arr) - 1):
		max_curr = max(arr[i], max_curr * arr[i])

		if max_curr > max_global:
			max_global = max_curr
	return max_global
def findTriplets(arr): 
    found = False
    n = len(arr)
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found") 

print(kadane([-2,3,-4]))
# findTriplets([0, -1, 2, -3, 1]) 
findTriplets([-1,0,1,2,-1,-4])
exit()
print(binary_sort([4,3,6,2,1]))
print(selection_sort([4,3,6,2,1,2]))
print(insertion_sort([4,3,6,2,1]))