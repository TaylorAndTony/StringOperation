import base64


def offset_char(text, offset):
    res = ''
    for i in text:
        res += chr(ord(i) + offset)
    return res


def b64encode(data):
    return base64.encodebytes(data.encode('utf-8')).decode('utf-8')


def b64decode(data):
    return base64.decodebytes(data.encode('utf-8')).decode('utf-8')


def encode(data):
    b64 = b64encode(data)
    off = offset_char(b64, -2)
    b64_2 = b64encode(off)
    return b64_2


def decode(data):
    b64 = b64decode(data)
    off = offset_char(b64, 2)
    b64_2 = b64decode(off)
    return b64_2


def read_txt():
    with open('website.txt', 'r', encoding='utf-8') as f:
        return f.read()


def decode_txt_to_new(target):
    with open(target, 'r', encoding='utf-8') as f:
        encoded = f.read()
    decoded = decode(encoded)
    with open('decoded.txt', 'w', encoding='utf-8') as f:
        f.write(decoded)


def encode_txt_to_new(target):
    with open(target, 'r', encoding='utf-8') as f:
        original = f.read()
    encoded = encode(original)
    with open('encoded.txt', 'w', encoding='utf-8') as f:
        f.write(encoded)


if __name__ == '__main__':
    encode_txt_to_new('./original.txt')
    decode_txt_to_new('./encoded.txt')
