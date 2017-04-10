count1 = 0
def merge_sort(a,b):
    c = []
    i = 0
    j = 0
    count = 0
    for k in range(len(a) + len(b)):
        if a[i]<b[j]:
            c = c + [a[i]]
            i = i+1
        else:
            c = c + [b[j]]
            j = j+1
            count = count + len(a) - i
        if i>len(a)-1:
            c = c + b[j:len(b)]
            break
        if j>len(b)-1:
            c = c + a[i:len(a)]
            break
    return c
def inversions(a,b):
    i = 0
    j = 0
    count = 0
    for k in range(len(a) + len(b)):
        if a[i]<=b[j]:
            i = i+1
        else:
            j = j+1
            count = count + len(a) - i
        if i>len(a)-1:
            break
        if j>len(b)-1:
            break
    return count

arr_file = open("C:\Users\dell  pc\Desktop\IntegerArray.txt", "r")
arr = map(int, arr_file.read().split())
ck = []
for l in range(len(arr)):
    ck.append([arr[l]])
while len(ck)>1:
    if len(ck)%2 != 0:
        arr1 = ck[0]
        arr2 = ck[1]
        ck[0] = merge_sort(arr1,arr2)
        del ck[1]
        count1 = count1 + inversions(arr1,arr2)
    else:
        d = []
        for l in range(0,len(ck),2):
            arr1 = ck[l]
            arr2 = ck[l+1]
            d.append(merge_sort(arr1,arr2))
            count1 = count1 + inversions(arr1,arr2)
        ck = d
    
print ck[0]
print count1
arr_file.close()