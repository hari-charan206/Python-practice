if __name__ == '__main__':
    L=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        L.append([name,score])
    sec=float('inf')
    low=float('inf')
    for i in L:
        if i[1]<low:
            sec=low
            low=i[1]
        elif i[1]>low and i[1]<sec:
            sec=i[1]
        else:
            pass
    l=[]
    for j in L:
        if j[1]==sec:
            l.append(j[0])
    l.sort()
    for k in l:
        print(k)

#Take 'n' input of name with score and display the names of students with the second least score
