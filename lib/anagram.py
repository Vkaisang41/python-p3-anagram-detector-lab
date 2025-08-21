class Anagram:
    def __init__(self, word: str):
        self.word = word
        self._norm = word.lower()
        self._signature = tuple(sorted(self._norm))

    def match(self, candidates):
        matches = []
        for cand in candidates:
            c_norm = cand.lower()
            if c_norm == self._norm:
                continue
            if tuple(sorted(c_norm)) == self._signature:
                matches.append(cand)
        return matches

