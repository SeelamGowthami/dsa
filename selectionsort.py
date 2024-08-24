def selection_sort(ar):
    for k in range(0,len(ar)):
        min_index=k 
        for j in range(k+1,len(ar)):
            if ar[j]<ar[min_index]:
                min_index=j 
        (ar[k],ar[min_index])=(ar[min_index],ar[k])
ar = [-2, 45, 0, 11, -9,88,-97,-202,747]
selection_sort(ar)
print(ar)