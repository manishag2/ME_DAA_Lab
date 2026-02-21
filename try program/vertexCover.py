import random
def vertex_cov(vertix,n):
    
    E=[i*1 for i in range(n)]
    print(E)
    ran_ver=[]
    for i in range(n):
        for j in range(n):
            ran_ver=[random.choice(E) for  _ in range(0,j)]
            for k in ran_ver:
                while(len(E)!=0):
                    if vertix[k][j]==1:
                        try:
                            E.remove(j)
                        except:
                            continue
                if E==0:
                    return ran_ver
        E=[i*1 for i in range(n)]




n=int(input("Enter the number of nodes:"))
vertix=[]
for i in range(n):
    arr=list(map(int,input(f"Enter the adjcent value of {i} as 1 remaining 0:").split()))
    vertix.append(arr)
print(vertix)
adj={}
adj_ver=[]
for i in range(n):
    for j in range(n):
        if vertix[i][j]!=0:
            adj_ver.append(j)
        adj[i]=adj_ver
    adj_ver=[]
print(adj)

vertix_x=vertex_cov(vertix,n)
print(vertix_x)