import json
import random
from pprint import pprint


class MessGenerator:
    def __init__(self, chars: str, min=5, max=15):
        self.chars = chars
        self.min = min
        self.max = max
        self.all_codes = self.__load_all_combining_chars()

    @staticmethod
    def __load_all_combining_chars() -> list:
        """ load all chars from a json file """
        with open('all_combining_chars.json', 'r', encoding='utf-8') as c:
            lst = json.load(c)
        code = [i.encode('utf-8') for i in lst]
        return code

    @staticmethod
    def __give_random_chars(chars, count_min, count_max):
        """ return a byte string of combining chars with random length """
        count = random.randint(count_min, count_max)
        r = bytes()
        for _ in range(count):
            r += random.choice(chars)
        return r

    def process(self) -> str:
        """ add all the letters to the top of each characters """
        res = bytes()
        for i in self.chars:
            res += i.encode('utf-8')
            res += self.__give_random_chars(self.all_codes, self.min, self.max)

        with open('result.txt', 'wb') as f:
            f.write(res)

        print(res.decode('utf-8'))


if __name__ == '__main__':
    gen = MessGenerator('杜易简', 5, 10)
    gen.process()
