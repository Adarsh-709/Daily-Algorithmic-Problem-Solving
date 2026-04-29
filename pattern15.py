'''
A B C D E
A B C D
A B C
A B
A
'''

class Solution:
    def pattern15(self, x: int):
        for i in range(x):
            start = 65
            for j in range(x,i,-1):
                print(chr(start),end=" ")
                start+=1
            print()
            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern15(x)
            