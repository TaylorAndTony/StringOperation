# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，
# 然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：


def calc_what_day(year, month, day):
    days = (
        31,
        28 if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else 29,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    )
    today = sum(days[:month - 1])
    today += day
    return today


temp = input('Type the date of today --> ')
a, b, c = temp.split(' ')
print('Today is the %d th day of this year' % calc_what_day(int(a), int(b), int(c)))
