'''
Problem Description: Given an integer N, write a program to print your name N times.
'''

class Solution:
    def sumNnums(self, n: int):
        if n==0:
            return 0
        return n + self.sumNnums(n-1)
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.sumNnums(n))

