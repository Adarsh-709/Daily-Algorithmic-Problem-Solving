'''
*****
*****
*****
*****
*****
'''
class Solution:
    def pattern1(self,x : int):
        for i in range(x):
            print("*" * x)

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern1(x)

