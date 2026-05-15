class Solution:
    def fibo(self, n: str) -> bool:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibo(n-1) + self.fibo(n-2)
        

if __name__ == '__main__':
    sol = Solution()
    n = int(input('Enter N: '))
    print(sol.fibo(n))