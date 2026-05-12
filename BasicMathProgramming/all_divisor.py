# Problem Statement: Given an integer N, return all divisors of N.

class Solution:
    def divisors(self, n: int):
        small = []
        large = []
        for i in range(1, int(n**0.5) + 1):
            if n%i==0:
                small.append(i)
                if i!=n//i:
                    large.append(n//i)
        return small + large[::-1]
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.divisors(n))