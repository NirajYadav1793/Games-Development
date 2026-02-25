arr = [2,3,4,1,5,7,6]
n = len(arr)

for i in range(n):
    for j in range(i,n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)