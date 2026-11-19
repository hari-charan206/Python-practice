class Solution {
public:
    int countOddDigit(int n) {
        int count=0;
        while(n>0){
            int last_digit=n%10;
            n=n/10;
            if(last_digit%2!=0){
                count+=1;
            }
        }
        return count;
    }
};

#This function takes a number and returns the count of number of odd digits present in the number 
