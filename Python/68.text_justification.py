class Solution:
    def _format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + ' ' * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        s, gap = line[0], len(line) - 1
        for index, w in enumerate(line[1:]):
            if index < (maxWidth - length) % gap:
                s = s + " " + " " * ((maxWidth - length) // gap) + w
            else:
                s = s + " " * ((maxWidth - length) // gap) + w
        return s
    
    def _formatLast(self, line, maxWidth):
        s = ' '.join(line)
        return s + ' ' * (maxWidth - len(s))
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        for word in words:
            if length + len(word) + len(line) <= maxWidth:
                length += len(word)
                line.append(word)
            else:
                res.append(self._format(line, maxWidth))
                length = len(word)
                line = [word]
        if len(line):
            res.append(self._formatLast(line, maxWidth))
        return res
