'''
*****
****
***
**
*
'''
class Solution:
    def pattern5(self,x : int):
        for i in range(x,0,-1):
            print("*" * i)

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern5(x)