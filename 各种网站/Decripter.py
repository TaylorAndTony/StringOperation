import base64


def encode(data):
    return base64.encodebytes(data.encode('utf-8')).decode('utf-8')


def decode(data):
    return base64.decodebytes(data.encode('utf-8')).decode('utf-8')


def read_txt():
    with open('website.txt', 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    txt = read_txt()
    dec = decode(txt)
    print(dec)
