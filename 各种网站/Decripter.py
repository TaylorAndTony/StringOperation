import base64


def encode(data):
    return base64.encodebytes(data.encode('utf-8')).decode('utf-8')


def decode(data):
    return base64.decodebytes(data.encode('utf-8')).decode('utf-8')


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
