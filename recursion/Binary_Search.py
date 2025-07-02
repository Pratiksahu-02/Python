def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

l=[]
a=int(input("How many elements do you want to enter in the array: "))
for i in range(a):
    l.append(int(input("Enter the element: ")))
target=int(input("Enter the element to search: "))
print(f"Element found at index {binary_search(l, target, 0, a-1)}")

# Example: binary_search([1, 2, 3, 4, 5], 4, 0, 4) should return 3