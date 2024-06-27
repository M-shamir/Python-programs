def selection_sort_desc(arr):
    for i in range(len(arr)):
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

size = int(input("Enter the size of an array: "))


arr = list(map(int, input("Enter the values of the array (comma-separated): ").split(',')))


if len(arr) != size:
    print("Error: The number of values entered does not match the specified size.")
else:
    
    selection_sort_desc(arr)

    print("Sorted array:")
    print(", ".join(map(str, arr)))
