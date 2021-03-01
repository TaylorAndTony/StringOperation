import random
import jieba


def just_mess(text) -> str:
    lst = list(text)
    random.shuffle(lst)
    return ''.join(lst)


def jieba_mess(text, filter_out_same = False) -> str:
    words = jieba.lcut(text)
    rand = words[:]
    random.shuffle(rand)
    final = []
    for first, second in zip(words, rand):
        final.append(first)
        final.append(second)
    if filter_out_same:
        final = list(set(final))
    return ''.join(final)



if __name__ == "__main__":
    a = just_mess('这是一个很神奇的文本编辑器')
    print(a)