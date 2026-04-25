'''
*
**
***
****
*****
****
***
**
*
'''

class Solution:
    def pattern10(self, x: int):
        for i in range(1,x*2):
            stars = i
            if i>x:
                stars = 2*x-i
            for j in range(stars):
                print("*",end="")
            print()




if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern10(x)
            