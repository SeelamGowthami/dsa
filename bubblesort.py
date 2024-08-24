def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(len(ar)-1):
            if ar[j]>ar[j+1]:
                (ar[j],ar[j+1])=(ar[j+1],ar[j])
ar = [-2, 45, 0, 11, -9,88,-97,-202,747]
bubble_sort(ar)
print(ar)