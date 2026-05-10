''' 
*********
 *******
  *****
   ***
    *
'''

class Solution:
    def pattern8(self,x : int):
        for i in range(x+1):
            for j in range(i):
                print(" ",end="")

            for k in range(2*x-(2*i-1)):
                print("*",end="")

            print()


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern8(x)