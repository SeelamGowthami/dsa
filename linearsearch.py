def linear_search(ar,key):
    for i in range(0,len(ar)):
        if ar[i]==key:
            return i
    return -1
ar = [1 ,3, 5, 4, 7, 9]  
key = 7 
res=linear_search(ar,key)

if res ==-1:
    print("element not found")
else:
    print("element found at",res) 