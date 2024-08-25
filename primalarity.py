def solve():
 n=int(input())
 if n==1:
    print("no")
 if n==2:
    print("yes")
 i=2
 while i*i<=n:
    if (n%i==0):
        print("no")
        break
    i+=1
else:
   print("yes")

t = 1
t = int(input())
for i in range(t):
    solve()
