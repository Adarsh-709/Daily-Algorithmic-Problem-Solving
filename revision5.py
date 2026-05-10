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
    def pattern(self, n: int):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top = i
                bottom = 2*n-i-2
                left = j
                right = 2*n-j-2
                d = min(top,bottom,left,right)
                print(n-d, end=" ")
            print()

if __name__=="__main__":
    sol = Solution()
    n = int(input())
    sol.pattern(n)