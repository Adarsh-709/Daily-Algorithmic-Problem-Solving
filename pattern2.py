'''
*
**
***
****
*****
'''



class Solution:
    def pattern2(self,x : int):
        for i in range(1,x+1):
            print("*" * i)

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern2(x)