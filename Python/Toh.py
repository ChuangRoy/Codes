a = int(input())
index = 0
def ToH(n , A, B, C):
    index = index+1
    if n==1:
        print(index, " Disk 1 from",A,"to",B)
        return 
    ToH(n-1, A, C, B)
    print(index, " Disk",n,"from",A,"to",B)
    ToH(n-1, C, B, A)
    
          
ToH(a,'A','B','C')
