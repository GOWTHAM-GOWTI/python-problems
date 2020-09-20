#display the index of the haystack if the needle in the haystack otherwise return -1 if the value=0 thn display 0

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        while needle in haystack:
            return haystack.find(needle)
        else:
            return -1

haystack= 'hello'
needle='l'
s=Solution()
sol=s.strStr(haystack,needle)
print(sol)