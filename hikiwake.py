import itertools
def eva(X):
    a,b,c,d,e,f,g,h,i=X[0],X[1],X[2],X[3],X[4],X[5],X[6],X[7],X[8]
    return abs(a+b+c)==3 or abs(d+e+f)==3 or abs(g+h+i)==3 or abs(a+d+g)==3 or abs(b+e+h)==3 or abs(c+f+i)==3 or abs(a+e+i)==3 or abs(c+e+g)==3

X=[0,1,2,3,4,5,6,7,8]
Y=list(itertools.permutations(X,9))
Z=[]
kosuu = 0
print(len(Y))
for A in Y:
    B=[0,0,0,0,0,0,0,0,0]
    for k in [0,2]:
        B[A[k]] = 1
        B[A[k+1]] = -1
    B[A[4]]=1
    if eva(B):
        continue
    
    B[A[5]]=-1
    if eva(B):
        continue
    
    B[A[6]]=1
    if eva(B):
        continue
        
    B[A[7]]=-1
    if eva(B):
        continue

    B[A[8]]=1
    if eva(B):
        continue
        
    kosuu += 1
    

print(kosuu)