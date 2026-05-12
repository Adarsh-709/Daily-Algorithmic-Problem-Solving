# Problem Statement: Given an integer N, check whether it is prime or not.

class Solution:
    def is_prime(self, n: int):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    


if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N : '))
    print(sol.is_prime(n))