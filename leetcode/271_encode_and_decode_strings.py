class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return chr(258)
        return chr(257).join(strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if s == chr(258):
            return []
        return s.split(chr(257))
