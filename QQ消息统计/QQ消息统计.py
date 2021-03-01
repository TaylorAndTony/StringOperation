from pprint import pprint, pp
import re


class QQMessageAnalyser:
    def __init__(self):
        """ Create an object to analyse messages """
        time_regex0 = r'\d\d?:\d\d:\d\d'
        name_regex0 = r'(.+?) \d\d?:\d\d:\d\d'
        self.time_regex = re.compile(time_regex0)
        self.name_regex = re.compile(name_regex0)
        self.mapping = []

    def analyse(self, file_path):
        """ analyse the given file """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        msg_group = data.split('\n\n')
        # ['刘佳乐 9:59:29\n【原神】荧妹出山 | 璃月的霄灯都是爷一人编的 https://b23.tv/f5IY2D',
        # '刘佳乐 10:24:14\n看好了，夜叉的力量是这样用的。 https://b23.tv/RMwBg5',
        # '刘佳乐 10:24:20\n@孙ly 学废了吗',
        for msg in msg_group:
            # 判断是否是有效消息
            if ' ' not in msg:
                continue
            # head: str 刘佳乐 9:59:29
            # 检测如果发送了空消息
            try:
                head, content = msg.split('\n')
            except ValueError:
                head = msg
                content = ''
            name = re.findall(self.name_regex, head)[0]
            send_time = re.findall(self.time_regex, head)[0]
            # print(name, send_time, content, sep='---')
            dct = {'name': name, 'time': send_time, 'content': content}
            self.mapping.append(dct)
        print(f'\033[32m{len(self.mapping)} analysed\033[0m')
    
    def quick_check(self, limit=None):
        """ quickly check the analysed data """
        if limit:
            mapping = self.mapping[:limit]
        else:
            mapping = self.mapping
        for group in mapping:
            print(group['name'], group['time'])
            print(group['content'])
            print()
    
    def who_send(self):
        """ list who has sent messages """
        senders = set()
        for group in self.mapping:
            name = group['name']
            senders.add(name)
        print(f'total {len(senders)} have sent message')
        pp(senders)

if __name__ == '__main__':
    qq = QQMessageAnalyser()
    qq.analyse('msg.txt')
    qq.quick_check()
