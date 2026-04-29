'''
A
B B
C C C
D D D D
E E E E E
'''

class Solution:
    def pattern16(self, x: int):
        start = 65
        for i in range(1,x+1):
            for j in range(i):
                print(chr(start),end=" ")
            start+=1
            print()
            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern16(x)
            