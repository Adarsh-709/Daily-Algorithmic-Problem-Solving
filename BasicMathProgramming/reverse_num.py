# Problem Statement: Given an integer N, return the number of digits in N.

class Solution:
    def reverse_number(self, n: int):
        reversed = 0
        while(n>0):
            ld = n%10
            reversed = reversed * 10 + ld
            n = n//10
        return reversed
        


if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.reverse_number(n))
