'''
1      1
12    21
123  321
12344321
'''

class Solution:
    def pattern12(self, x: int):
        for i in range(1,x+1):
            
            #numbers
            for j in range(1,i+1):
                print(j, end="")
            

            #spaces
            for k in range(2*x-2*i):
                print(" ",end="")

            #numbers
            for j in range(i,0,-1):
                print(j, end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern12(x)
            