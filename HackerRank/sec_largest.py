if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lar=0
    sec=0
    if n>=2 and n<=10 :
        for i in arr:
            if i>lar:
                lar=i
        for j in arr:
            if j<lar and j>sec:
                sec=j
        print(sec)

#Take an input 'n' followed by 'n' numbers and display the second largest number from the given numbers
