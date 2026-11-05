class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_letters_s = [0 for i in range(26)]
        count_letters_t = [0 for i in range(26)]
        for letter in s:
            count_letters_s[ord(letter) - ord('a')] += 1
        for letter in t:
            count_letters_t[ord(letter) - ord('a')] += 1
        return count_letters_s == count_letters_t