'''
1
12
123
1234
12345
'''

class Solution:
    def pattern3(self,x : int):
        for i in range(1,x+1):
            for j in range(i):
                print(j+1,end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern3(x)