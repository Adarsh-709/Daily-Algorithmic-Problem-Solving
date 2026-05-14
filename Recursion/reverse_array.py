'''
Problem Description: Given an integer N, write a program to print your name N times.
'''

class Solution:
    def rev_array(self, arr: list ,n: int):
        if n==0:
            return
        print(arr[n-1])
        self.rev_array(arr,n-1)
        

if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,4,5]
    n = len(arr)
    sol.rev_array(arr,n)

