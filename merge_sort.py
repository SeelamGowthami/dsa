def merge(ar, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = ar[p + i]
    for j in range(n2):
        R[j] = ar[q + 1 + j]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            ar[k] = L[i]
            i += 1
        else:
            ar[k] = R[j]
            j += 1
def mergesort(ar, p, r):
    if p < r:
        q = (p + r) // 2
        mergesort(ar, p, q)
        mergesort(ar, q + 1, r)
        merge(ar, p, q, r)
#ar = list(map(int, input("Enter the list of integers (space separated): ").split()))
ar=[2, 10, 1 ,3, 5, 9 ,12 ,11]
print("original arry:",ar)
mergesort(ar, 0, len(ar) - 1)
print("Sorted array:", ar)
