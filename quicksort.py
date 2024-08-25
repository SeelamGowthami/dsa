def partition(ar,p,r):
    pivot=ar[r]
    i=p-1
    for j in range(p,r):
        if ar[j]<=pivot:
            i=i+1
            (ar[i],ar[j])=(ar[j],ar[i])
    (ar[i+1],ar[r])=(ar[r],ar[i+1])
    return i+1
def quick_sort(ar,p,r):
    if(p<r):
        q=partition(ar,p,r)
        quick_sort(ar,p,q-1)
        quick_sort(ar,q+1,r)
ar=[2, 10, 1 ,3, 5, 9 ,12 ,11]
print("original arry:",ar)
quick_sort(ar, 0, len(ar) - 1)
print("Sorted array:", ar)


