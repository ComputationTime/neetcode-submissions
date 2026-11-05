class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for word in strs:
            letter_count = [0 for _ in range(26)]
            for letter in word:
                letter_count[ord(letter) - ord('a')] += 1
            group : List[str] = groups.get(tuple(letter_count), [])
            group.append(word)
            groups[tuple(letter_count)] = group
        return list(groups.values())