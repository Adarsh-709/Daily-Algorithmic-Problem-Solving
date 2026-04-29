'''
   *
  * *
 *   *
*     *
*     *
 *   *
  * *
   *
'''

class Solution:
    def pattern23(self, x: int):
        for i in range(2*x):
            d = min(i,2*x-i-1)
            o_spaces = x-d-1
            i_spaces = 2*d-1
            if d==0:
                print(" "*o_spaces + "*")
            else:
                print(" "*o_spaces + "*" + " "*i_spaces + "*")

            


        



if __name__ is "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern23(x)

