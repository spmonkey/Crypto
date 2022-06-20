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
from decode.low_decryption_exponent_attack import RSA_wiener
import lib.help_info
import sys
import re

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
        elif sys.argv[1] == '--low':
            n = input("n = ")
            n1 = []
            c = input("c = ")
            e = int(input("e = "))
            n = re.sub("\[", "", n)
            n = re.sub(']', "", n)
            n = n.split(',')
            for i in n:
                n1.append(int(i))
            c = re.sub("\[", "", c)
            c = re.sub(']', "", c)
            c = c.split(',')
            c1 = []
            for i in c:
                c1.append(int(i))
            print('\n[+]正在解密...')
            decode = RSA_wiener(n=n1, e=e, c=c1)
            decode.CRT()
        else:
            lib.help_info.help_info()
    except:
        lib.help_info.help_info()

if __name__ == "__main__":
    main()
