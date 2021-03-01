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


##############################
#        高级加密方法          #
##############################

def offsite_three_key(content: str) -> str:
    """
    123变密钥凯撒加密
    :param content: 待加密字符串
    :return: 变密钥加密后的字母
    """
    # 自定义两个参数，请确保加密解密参数相同
    prefix = PREFIX  # 方便测试使用
    gap = GAP  # 实际可复制该函数，确保加密解密这两个参数一致

    lst = []
    offsite = prefix
    for each_char in content:
        offsite += gap
        if offsite == prefix + gap * 4:  # 其实就是三个一循环
            offsite = prefix + 1
        lst.append(ord(each_char) + offsite)
    res = ''
    for each_code in lst:
        res += chr(each_code)
    return res


def solve_three_key(content):
    """
    123变密钥凯撒解密
    :param content: 经变密钥加密后的字符串
    :return: 解密后的字符串
    """
    lst = []
    for each_letter in content:
        lst.append(ord(each_letter))

    prefix = PREFIX  # 方便测试使用
    gap = GAP  # 实际可复制该函数，确保加密解密这两个参数一致

    res = ''
    offsite = prefix
    for each_item in lst:
        offsite += gap
        if offsite == prefix + gap * 4:  # 其实就是三个一循环
            offsite = prefix + 1
        res += chr(each_item - offsite)
    return res


if __name__ == '__main__':
    PREFIX = 486
    GAP = -1

    test = 'Hello world there, this is a string'
    print('原始字符串为\t%s' % test)
    a = offsite_three_key(test)
    print('加密后的字符串为\t%s' % a)
    b = solve_three_key(a)
    print('解密后的字符串为\t%s' % b)
