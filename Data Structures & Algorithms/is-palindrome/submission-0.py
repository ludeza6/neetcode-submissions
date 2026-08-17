class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstr = "".join(char for char in s if char.isalnum()).lower()
        return cleanstr == cleanstr[::-1]