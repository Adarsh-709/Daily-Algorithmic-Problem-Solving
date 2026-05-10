'''
      A
    A B A
  A B C B A
A B C D C B A
'''

class Solution:
    def pattern17(self, x: int):
        for i in range(1,x+1):
            start = 64

            #space
            for k in range(x-i):
                print(" ",end="")

            #char
            for j in range(2*i-1):
                if j>=i:
                    start-=1
                else:
                    start+=1
                print(chr(start),end = "")
                
            print()


            #space
            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern17(x)
            