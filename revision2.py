'''
   1
  212
 32123
4321234
'''

class Solution:
    def pattern(self, n: int):
        for i in range(n):
            start = i+1
            print(" "*(n-i-1),end="")
            for j in range(2*i+1):
                print(start,end="")
                if j>=i:
                    start+=1
                else:
                    start-=1
            print()

if __name__=="__main__":
    sol = Solution()
    n = int(input())
    sol.pattern(n)