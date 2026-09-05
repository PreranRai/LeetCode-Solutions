class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]

            # If word starts with a consonant
            if word[0] not in vowels:
                word = word[1:] + word[0]

            # Add "ma"
            word = word + "ma"

            # Add 'a' based on position
            word = word + "a" * (i + 1)

            result.append(word)

        return " ".join(result)