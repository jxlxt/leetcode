import collections
class Solution:
    # time complexity: O(C^2) where CC is the number of characters across all words in the given array.
    # space complexity: O(C)
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        abbreviations = [''] * len(words)
        duplicates    = collections.defaultdict(list)
        for i,word in enumerate(words):
            abbreviations[i] = self.get_abbreviation(word,'')
            duplicates[abbreviations[i]] += i,
        
        for i in range(len(abbreviations)):
            if len(duplicates[abbreviations[i]]) == 1:
                continue
            else:
                while len(duplicates[abbreviations[i]]) > 1:
                    for index in duplicates[abbreviations[i]]:
                        abbreviation = self.get_abbreviation(words[index], abbreviations[index])
                        abbreviations[index] = abbreviation
                        duplicates[abbreviation] += index,
                        
        return abbreviations
    
    def get_abbreviation(self, word, old_abbreviation):
            if old_abbreviation == '':
                abbreviation = word[0] + str(len(word[1:-1])) + word[-1]                
            else:
                for i in range(len(old_abbreviation)):
                    if old_abbreviation[i].isdigit():
                        abbreviation = word[:i+1] + str(len(word[i+1:-1])) + word[-1]
                        break
            if len(word) <= len(abbreviation):
                abbreviation = word
            return abbreviation
        
# there should be a faster solution Group + Trie
