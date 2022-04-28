# coding utf-8
import os
import chardet


# 获得所有java文件的路径,传入根目录路径
def find_all_file(path: str) -> str:
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.htm'):
                fullname = os.path.join(root, f)
                yield fullname
            pass
        pass
    pass


# 判断是不是utf-8编码方式
def judge_coding(path: str) -> dict:
    with open(path, 'rb') as f:
        c = chardet.detect(f.read())

    print(c)

    if c['encoding'] != 'utf-8':
        return c


# 修改文件编码方式
def change_to_utf_file(path: str):
    for i in find_all_file(path):
        c = judge_coding(i)
        if c:
            change(i, c['encoding'])
            print("{} 编码方式已从{}改为 utf-8".format(i, c['encoding']))


def change(path: str, coding: str):
    print(path)
    print(coding)
    if coding=='GB2312':
        coding='GB18030'
    with open(path, 'r', encoding=coding) as f:
        text = f.read()

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


# 查看所有文件编码方式
def check(path: str):
    for i in find_all_file(path):
        with open(i, 'rb') as f:
            print(chardet.detect(f.read())['encoding'], ': ', i)


def main():
    my_path = '/home/urna/dev/Chan/'
    change_to_utf_file(my_path)
    # check(my_path)


if __name__ == '__main__':
    main()
