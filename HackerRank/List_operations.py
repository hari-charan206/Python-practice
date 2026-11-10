if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(N):
        n=input()
        s=n.split()
        if s[0].lower()=="insert":
            L.insert(int(s[1]),int(s[2]))
        elif s[0].lower()=="remove":
            L.remove(int(s[1]))
        elif s[0].lower()=="append":
            L.append(int(s[1]))
        elif s[0].lower()=="sort":
            L.sort()
        elif s[0].lower()=="pop":
            L.pop()
        elif s[0].lower()=="reverse":
            L.reverse()
        elif s[0].lower()=="print":
            print(L)
        else:
            pass

'''
Give value 'n' followed by 'n' number statements containing commands to edit the list
using the commands: insert i e, remove e, append e, sort, pop, reverse,print
i=index, e=element
'''
