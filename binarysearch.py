l=[2,4,6,8,14,25,56]
target=25
low=0
high=len(l)
while low <= high:
    mid = (low + high) // 2
    if l[mid] == target:
        print("element found at", mid)
        break
    elif target < l[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("element not found")
        