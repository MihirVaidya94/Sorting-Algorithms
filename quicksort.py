def swap(x,y):
	temp = x
	x = y
	y = temp
	return (x,y)

def quicksort(arr,l):
	if len(arr)%2 == 0:
		t = [arr[0], arr[len(arr)/2 - 1], arr[len(arr)-1]]
		t.sort()
		if t[1] == arr[0]:
			pivot = 0
		elif t[1] == arr[len(arr)/2 - 1]:
			pivot = len(arr)/2 - 1
		else:
			pivot = len(arr)-1
	else:
		t = [arr[0], arr[len(arr)/2], arr[len(arr)-1]]
		t.sort()
		if t[1] == arr[0]:
			pivot = 0
		elif t[1] == arr[len(arr)/2]:
			pivot = len(arr)/2
		else:
			pivot = len(arr)-1
	i = 0
	m = 1
	arr[0],arr[pivot] = swap(arr[0],arr[pivot])
	for k in range(m,len(arr)):


	    if arr[k] <= arr[0]:
	    	i = i+1
	    	arr[i],arr[k] = swap(arr[i],arr[k])
	arr[0],arr[i] = swap(arr[0],arr[i])
	return arr,i+l,len(arr)-1

arr_file = open("C:\Users\dell  pc\Desktop\QuickSort.txt", "r")
num_list = map(int, arr_file.read().split())
pivots = [-1,len(num_list)]
j = 0
count = 0
while pivots[j] < len(num_list):	
	while len(num_list[pivots[j]+1:pivots[j+1]]) > 1:
		num_list[pivots[j]+1:pivots[j+1]],k,l = quicksort(num_list[pivots[j]+1:pivots[j+1]],pivots[j]+1)
		pivots = pivots[:j+1] + [k] + pivots[j+1:]
		count = count + l
	j = j+1
print num_list
print count