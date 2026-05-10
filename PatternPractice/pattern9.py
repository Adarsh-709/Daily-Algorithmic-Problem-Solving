''' 
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''

class Solution:
    def pattern9(self,x : int):
        for i in range(x+1):
            for j in range(x-i):
                print(" ",end="")

            for k in range(i+i+1):
                print("*",end="")

            print()

        for i in range(x+1):        
            for j in range(i):
                print(" ",end="")

            for k in range(2*x-(2*i-1)):
                print("*",end="")

            print()


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern9(x)