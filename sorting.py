def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [5, 2, 8, 1, 3]

print("Original list:", numbers)
print("Sorted list:", bubble_sort(numbers))