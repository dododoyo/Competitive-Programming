class Solution {                      
public:
    int reverse(int x) {
        long r=0;      // decleare r 
        while(x){
         r=r*10+x%10; // find reminder and add its to r
         x=x/10;     // Update the value of x
        }
        if(r>INT_MAX || r<INT_MIN) return 0; // check 32 bit range 
        return int(r);
    }
}; 