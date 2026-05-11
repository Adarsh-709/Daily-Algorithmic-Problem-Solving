# Problem Statement: Given an integer N, return the number of digits in N.

class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        if x<0:
            x = -x
            sign = -1
        else:
            sign = 1
        while(x>0):
            last_digit = x%10
            rev_num = rev_num * 10 + last_digit
            x = x//10
        rev_num *= sign
        return rev_num if -2**31  <= rev_num <= 2**31 - 1 else 0
        
        


if __name__ == '__main__':
    sol = Solution()
    x = int(input('Enter N : '))
    print(sol.reverse(x))
