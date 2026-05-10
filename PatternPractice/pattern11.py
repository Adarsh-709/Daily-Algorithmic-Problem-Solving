'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

class Solution:
    def pattern11(self, x: int):
        start = 1
        for i in range(x):
            if i%2 == 0:
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(start,end=" ")
                start = 1 - start
            print()
            




if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern11(x)
            