'''
1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7
'''

class Solution:
    def pattern(self, n: int):
        mat = [[0]*n for _ in range(n)]
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        num = 1
        while top <= bottom and left <= right:
            for i in range(top,right+1):
                mat[top][i] = num
                num += 1
            top+=1
            for j in range(top, bottom+1):
                mat[j][right] = num
                num+=1 
            right -= 1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    mat[bottom][i] = num
                    num+=1
                bottom-=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    mat[i][left]=num
                    num+=1
                left += 1

        for i in range(n):
            for j in range(n):
                print(mat[i][j],end = " ")
            print()

if __name__=="__main__":
    sol = Solution()
    n = int(input())
    sol.pattern(n)