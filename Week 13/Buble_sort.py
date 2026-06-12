def buble_sort (arr):
    n = len(arr)
    for i in range(n):
        print(f"pass {i + 1}: {arr}")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
arr = [64, 34, 25, 12, 22, 11, 90]
buble_sort(arr)
print("sorted array:", arr)
        