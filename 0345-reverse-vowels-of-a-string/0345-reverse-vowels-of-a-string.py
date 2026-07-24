class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"

        chars = list(s)
        v = []

        # Collect vowels
        for ch in chars:
            if ch in vowels:
                v.append(ch)

        v.reverse()

        # Replace vowels
        j = 0
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = v[j]
                j += 1

        return "".join(chars)