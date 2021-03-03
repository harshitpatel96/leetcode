class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}

        longest_substring = -1
        for idx, char in enumerate(s):
            if char in char_map:
                longest_substring = max(longest_substring, idx - char_map[char]-1) 

            else:
                char_map[char] = idx

        return longest_substring
