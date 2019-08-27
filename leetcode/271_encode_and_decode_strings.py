class Codec:

    def encode(self, strs):
        return ''.join(self.len_to_str(len(s)) + s.encode('utf-8')
                       for s in strs)

    def decode(self, s):
        strs = []
        i, N = 0, len(s)
        while i < N:
            curr_len = self.str_to_len(s[i:i+4])
            i += 4
            strs.append(s[i:i+curr_len])
            i += curr_len
        return strs

    def len_to_str(self, val):
        return format(val, '04d')

    def str_to_len(self, s):
        return int(s)
