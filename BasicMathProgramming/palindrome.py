# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

class Solution:
    def palindrome(self, n):
        if n<0:
            sign = -1
            n = -n
        else:
            sign =1
        num = n
        rev = 0
        while(num != 0):
            ld = num % 10
            rev = rev * 10 + ld
            num = num // 10
        return True if rev==n else False

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter n : '))
    print(sol.palindrome(n))