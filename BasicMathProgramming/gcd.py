# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

class Solution:
    def gcd(self, n1, n2):
        while n1>0 and n2>0:
            if n1>n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
        return n2 if n1==0 else n1
        

if __name__ == '__main__':
    sol = Solution()
    n1 = int(input('Enter n1 : '))
    n2 = int(input('Enter n2 : '))

    print(sol.gcd(n1,n2))