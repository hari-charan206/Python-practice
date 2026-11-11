def swap_case(s):
    L=[]
    for i in range(0,len(s)):
        if s[i].islower():
            L.append(s[i].upper())
        else:
            L.append(s[i].lower())
    return ''.join(L)

if __name__ == '__main__':

#Swaps the case of the string
