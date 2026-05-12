# Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.
import math

class Solution:
    def is_armstrong(self, n: int):
        power = int(math.log10(n) + 1)
        dup_n = n
        arm = 0
        while(n!=0):
            ld = n%10
            arm += ld**power
            n = n//10
        return True if arm==dup_n else False
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.is_armstrong(n))