'''
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *

'''

class Solution:
    def pattern20(self, x: int):
        for i in range(1,2*x):
            #stars
            if i<=x:
                stars = i
                spaces = (2*x)-(2*i)
            else:
                stars = 2*x-i
                spaces = (2*i)-(2*x)
            
            print("*"*stars + " "*spaces + "*"*stars)

if __name__ is "__main__":
    sol = Solution()
    x = int(input())
    sol.pattern20(x)