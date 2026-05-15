'''
Problem Description: Given an integer N, write a program to print your name N times.
'''

class Solution:
    def rev_array(self, arr: list , i: int):
        if i==(len(arr)//2):
            return arr
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
        return self.rev_array(arr,i+1)        

if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,4,5]
    print(sol.rev_array(arr,0))

