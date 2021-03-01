def offsite_char(var: str, offsite) -> list:
    """
    给定密钥的凯撒加密
    :param var:待加密字符串
    :param offsite:密钥
    :return:ASCII数字列表
    """
    ascii_code = []
    for i in var:
        ascii_code.append(ord(i) + offsite)
    return ascii_code


def translate_offsite(lst, key):
    """
    解密一个凯撒加密后的整数列表
    :param lst: 整数列表（已被加密）
    :param key: 解密密钥，加密密钥的负数
    :return: 解密完成的字符串
    """
    temp = ''
    for i in lst:
        temp += str(chr(i + key))
    return temp


#################################################

def offsite_three_key(content: str) -> list:
    """
    123变密钥凯撒加密
    :param content: 待加密字符串
    :return: 变密钥加密后的整数列表
    """
    lst = []
    offsite = -1
    for each_char in content:
        offsite += 1
        if offsite == 3:
            offsite = 0
        lst.append(ord(each_char) + offsite)
    return lst


def solve_three_key(lst: list):
    """
    123变密钥凯撒解密
    :param lst: 经变密钥加密后的整数列表
    :return: 解密后的字符串
    """
    res = ''
    offsite = -1
    for each_item in lst:
        offsite += 1
        if offsite == 3:
            offsite = 0
        res += chr(each_item - offsite)
    return res


if __name__ == '__main__':
    a = offsite_three_key('aaaaaaaaaaaaa')
    print(a)
    b = solve_three_key(a)
    print(b)
