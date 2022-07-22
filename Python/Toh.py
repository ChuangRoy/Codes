a = int(input())
def ToH(n , A, B, C, i):
    if n == 1:
        i = i + 1
        print(i, " Disk 1 from",A,"to",B)
        return i
    i = ToH(n-1, A, C, B, i)
    i = i + 1
    print(i, " Disk",n,"from",A,"to",B)
    i = ToH(n-1, C, B, A, i)
    return i
          
ToH(a,'A','B','C', 0)
