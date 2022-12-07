import openpyxl


def func_main():
    t1()
    pass


def t1():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Top250'
    ws.append(('标题', '评分', '主题'))
    items = [('标题', '分数', '主题'), ('标题1', '分数2', '主题3'), ]
    for item in items:
        title, score, subject = item
        ws.append((title, score, subject))
    wb.save('电影数据.xlsx')
