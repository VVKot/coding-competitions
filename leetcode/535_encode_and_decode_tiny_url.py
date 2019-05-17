import string
import random


class Codec:

    symbols = string.ascii_lowercase + '0123456789'

    def __init__(self):
        self.code_to_url = {}

    def get_random_code(self, count):
        return ''.join([random.choice(Codec.symbols) for _ in range(count)])

    def encode(self, longUrl):
        code = ""
        while not code:
            random_code = self.get_random_code(6)
            if random_code not in self.code_to_url:
                code = random_code
                self.code_to_url[code] = longUrl
        return 'https://tinyurl.com/{}'.format(code)

    def decode(self, shortUrl):
        code = shortUrl[-6:]
        return self.code_to_url[code]
