def insertion_sort(ar):
    for i in range(1,len(ar)):
        key=ar[i]
        j=i-1
        while j>=0 and key<ar[j]:
            ar[j+1]=ar[j]
            j-=1
        ar[j+1]=key 
ar= [-2, 45, 0, 11, -9,88,-97,-202,747]
insertion_sort(ar)
print(ar)
