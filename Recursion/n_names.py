'''
Problem Description: Given an integer N, write a program to print your name N times.
'''

class Solution:
    def n_name_rec(self, name, n: int):
        if n==0:
            return
        print(name)
        return self.n_name_rec(name, n-1)
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    name = 'Adarsh'
    sol.n_name_rec(name,n)

