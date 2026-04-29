'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

class Solution:
    def pattern18(self, x: int):
        space = 0
        stars = 0
        for i in range(1,x+1):

            if i<=x//2:
                stars = (x//2)-i+1
            else:
                stars = i-(x//2)
            
            print("*" * stars, end="")
            print(" " * space, end="")
            print("*" * stars, end="")

            if i<x//2:
                space += 2
            elif i >= x//2 + 1:
                space -= 2

            print()

            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern18(x)
            