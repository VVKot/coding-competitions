from typing import List


class Solution:

    def replaceWords(self, roots: List[str], sentence: str) -> str:
        roots.sort()
        result = []
        for word in sentence.split():
            for root in roots:
                if word.startswith(root):
                    result.append(root)
                    break
            else:
                result.append(word)
        return ' '.join(result)
