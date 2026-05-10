'''
12345
1234
123
12
1
'''

class Solution:
    def pattern6(self,x : int):
        for i in range(x,0,-1):
            for j in range(1,i+1):
                print(j,end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern6(x)