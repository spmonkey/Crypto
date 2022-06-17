'''
Function:
    RSA解密算法帮助
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hscsec.cn
'''
# -*- coding:utf-8 -*-
import sys

def help_info():
    help = """
usage : python {0} [--参数]
    --RSA_n       自带对 n 的因式分解，仅需提供 n、e、c.
    --RSA         需提供 p、q、n、e、c.
    --common      RSA同模攻击.
""".format(sys.argv[0])
    print(help)