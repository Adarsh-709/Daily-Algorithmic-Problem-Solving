'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

class Solution:
    def pattern13(self, x: int):
        start = 1
        for i in range(1,x+1):
            for j in range(1,i+1):
                print(start,end=" ")
                start+=1
            print()


if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern13(x)
            