# Problem Statement: Given an integer N, return the number of digits in N.
import math

class Solution:
    def count_digits(self, n: int):
        count = 0
        while(n>0):
            n = n//10
            count+=1
        return count + 1
    
    def count_digits_optimal(self, n: int):
        count = int(math.log10(n)) + 1
        return count


if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.count_digits_optimal(n))