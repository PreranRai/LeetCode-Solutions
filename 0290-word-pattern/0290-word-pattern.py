class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_indexes = list(map(pattern.index, pattern))
        word_indexes = list(map(words.index, words))

        if pattern_indexes == word_indexes:
            return True
        else:
            return False