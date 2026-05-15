
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
                return True
        s = s.lower()
        dup_s = ""
        for x in s:
            if ord('a')<=ord(x)<=ord('z'):
                dup_s += x
        print(dup_s, dup_s[::-1])
        return True if dup_s==dup_s[::-1] else False       

if __name__ == '__main__':
    sol = Solution()
    s = input('Enter String: ')
    print(sol.isPalindrome(s))