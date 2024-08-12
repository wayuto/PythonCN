#!/usr/bin/python
from base import *
import key_word as k
import sys
import os


def exec_file(file):
    data = ''
    with open(f"{file}", "r") as f:
        data = f.read()
        #print(data)

        for i, j in k.key_word.items():
            data = data.replace(j, i)
    try:
        exec(data)
    except Exception as ex:
        print(ex)

def cli():
    print('PythonCN 1.0.0 Linux平台')
    print('欢迎使用PythonCN')
    while True:
        try: 
            code = input('>>> ')
            if code == '退出':
                break
            exec(code)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    __name__ = '__主干__'
    __名字__ = __name__
    if len(sys.argv) > 1:
        if sys.argv[1] == '-c':
            if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
                exec_file(sys.argv[2])
            else:
                print('你的*.pc文件呢?')
        elif sys.argv[1] == '-v':
            print('PythonCN 版本: 1.0.0')
    else:
        cli()

