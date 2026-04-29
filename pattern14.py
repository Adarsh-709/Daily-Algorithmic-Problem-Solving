'''
A
A B
A B C
A B C D
A B C D E
'''

class Solution:
    def pattern14(self, x: int):
        for i in range(1,x+1):
            start = 65
            for j in range(i):
                print(chr(start),end=" ")
                start+=1
            print()
            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern14(x)
            