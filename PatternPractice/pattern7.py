'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

class Solution:
    def pattern7(self,x : int):
        for i in range(x):
            for j in range(x-i):
                print(" ",end="")
            for k in range(i+1):
                print("* ",end="")

            print()


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern7(x)