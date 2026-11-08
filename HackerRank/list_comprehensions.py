if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    L=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                e=[]
                e.append(i)
                e.append(j)
                e.append(k)
                L.append(e)
    s=[]
    for p in L:
        o=0
        for q in p:
            o+=q
        if o<n or o>n:
            s.append(p)
        else:
            continue
    print(s)


'''Each variable x, y and z will have values of 0 or 1. All permutations of lists in the form [i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]].

Remove all arrays that sum to n = 2 to leave only the valid permutations.'''
