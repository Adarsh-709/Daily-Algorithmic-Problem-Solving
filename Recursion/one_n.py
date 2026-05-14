'''
Problem Description: Given an integer N, write a program to print your name N times.
'''

class Solution:
    def oneToN(self, n: int):
        if n==0:
            return
        self.oneToN(n-1)
        print(n)
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    sol.oneToN(n)

