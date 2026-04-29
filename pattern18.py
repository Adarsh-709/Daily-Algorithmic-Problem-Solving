'''
E
D E
C D E
B C D E
A B C D E
'''

class Solution:
    def pattern18(self, x: int):
        start = ord('E')
        for i in range(x):
            for j in range(i+1):
                print(chr(start+j),end=" ")
            start-=1
            print()
            


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern18(x)
            