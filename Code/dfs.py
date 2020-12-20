n=2
N=101
def dfs(i,sum):
    if i==n+1:
        if sum==100:
            ans+=1
            return
    for j in range(N):
        dfs(i+1,sum+j)
    return ans

dfs(1,0)
