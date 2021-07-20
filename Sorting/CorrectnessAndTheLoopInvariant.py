

def insertion_sort(arr):
    for i in range(1, len(arr)):
        index = i
        while arr[index - 1] > arr[index] and index > 0:
            temp = arr[index - 1]
            arr[index - 1] = arr[index]
            arr[index] = temp
            index -= 1

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))