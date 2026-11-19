class Solution {
public:
    int largestDigit(int n) {
        int largest=n%10;
        while(n>0){
            int last=n%10;
            if(last>largest) largest=last;
            n=n/10;
        }
        return largest;
    }
};

#The function takes a number as input and returns the largest digit present in the number
