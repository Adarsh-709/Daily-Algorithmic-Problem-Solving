'''
   1
  123
 12355
1234777
1234777
 12355
  123
   1
'''

class Solution:
    def pattern24(self, x: int):
        for i in range(2*x):
            d = min(i,2*x-i-1)
            spaces = x-d-1
            print(" "*spaces, end="")
            for j in range(2*d+1):
                    print(1+j if j<=d else 2*d+1,end="")
            print()
            

if __name__ is "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern24(x)