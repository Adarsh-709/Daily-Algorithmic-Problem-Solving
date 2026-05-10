'''
1
22
333
4444
55555
'''
class Solution:
    def pattern4(self,x : int):
        for i in range(1,x+1):
            for j in range(i):
                print(i,end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern4(x)