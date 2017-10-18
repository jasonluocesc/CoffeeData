def find_pair(A):
    length = len(A) // 2
    print("length=",length)
    if length==0:
        print("No index")
        return 0
    elif A[length]==length:
        print(length)
        return length
    elif A[length] > length:
        return find_pair(A[0:length])
    elif A[length]< length:
        return find_pair(A[length:])


A=[-1,0,2,3]
find_pair(A)



