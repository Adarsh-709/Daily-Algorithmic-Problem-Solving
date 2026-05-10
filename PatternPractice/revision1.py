'''
   *
  * *
 *   *
*     *
 *   *
  * *
   *
'''

class Solution:
    def pattern(self, n: int):
        for i in range(2*n-1):
            d = min(i, 2*n-i-2)
            o_spaces = n-d-1
            i_spaces =  2*d-1
            if d==0:
                print(" "*o_spaces + "*")
            else:
                print(" "*o_spaces + "*" + " "*i_spaces + "*")




if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    sol.pattern(n)