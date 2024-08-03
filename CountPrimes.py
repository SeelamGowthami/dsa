 def countPrimes(self, n: int) -> int:
        pr=[True]*n
        if n==0 or n==1:
            return 0
        pr[0]=False
        pr[1]=False
        for i in range(2,n):
            if(pr[i]==True):
                for j in range(2*i,n,i):
                    pr[j]=False
        return sum(pr)