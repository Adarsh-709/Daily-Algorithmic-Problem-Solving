'''
1
0 1
1 0 1
0 1 0 1
'''

class Solution:
    def pattern(self, n: int):
        for i in range(n):
            for j in range(i + 1):
                print(1-(i + j) % 2, end=" ")
            print()

if __name__=="__main__":
    sol = Solution()
    n = int(input())
    sol.pattern(n)