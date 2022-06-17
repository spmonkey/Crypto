'''
Function:
    RSA解密工具
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hscsec.cn
'''
# -*- coding:utf-8 -*-
from decode.RSA_n_factoring import RSA_n
from decode.RSA import RSA
from decode.common_modulus_attack import common_modulus
import lib.help_info
import sys

def main():
    try:
        # 不知道 p和q 的
        if sys.argv[1] == '--RSA_n':
            n = int(input("n = "))
            e = int(input("e = "))
            c = int(input("c = "))
            decode = RSA_n(n=n, e=e, c=c)
            decode.n_factoring()
        # 知道 p和q 的
        elif sys.argv[1] == '--RSA':
            p = input("p = ")
            q = input("q = ")
            n = input("n = ")
            e = input("e = ")
            c = input("c = ")
            decode = RSA(n=n, e=e, c=c, p=p, q=q)
            decode.rsa_k()
        # RSA共模攻击
        elif sys.argv[1] == '--common':
            n = input("n = ")
            e1 = input("e1 = ")
            c1 = input("c1 = ")
            e2 = input("e2 = ")
            c2 = input("c2 = ")
            decode = common_modulus(n=n, e1=e1, c1=c1, e2=e2, c2=c2)
            decode.RSA_common_modulus_attack()
        else:
            lib.help_info.help_info()
    except:
        lib.help_info.help_info()

if __name__ == "__main__":
    main()