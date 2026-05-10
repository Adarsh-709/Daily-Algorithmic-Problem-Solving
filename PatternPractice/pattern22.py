'''
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''

class Solution:
    def pattern22(self,x: int):
        for i in range(2*x-1):
            for j in range(2*x-1):
                d = min(i, j, 2*x-i-2, 2*x-j-2)
                print(x-d,end=" ")
            print()

if __name__ is "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern22(x)