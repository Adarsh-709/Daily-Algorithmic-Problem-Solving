''' 
*****
*   *
*   *
*   *
*****
'''

class Solution:
    def pattern21(self, x: int):
        for i in range(1,x+1):
            for j in range(1,x+1):
                print("*" if i in (1,x) or j in (1,x) else " ",end="")
            print()


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern21(x)