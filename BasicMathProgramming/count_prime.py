class Solution:
    def countPrimes(self, n: int) -> int:
        ictn = 0
        for i in range(2,n):
            if i==2 or i == 3:
                ictn+=1
                continue
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
                elif j==int(i**0.5):
                    print(i)
                    ictn+=1
        return ictn


if __name__ == '__main__':
    sol = Solution()
    x = int(input('Enter N : '))
    print(sol.countPrimes(x))
