'''
Function:
    RSA解密算法
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hscsec.cn
Github:
    https://github.com/spmonkey/
'''
# -*- coding:utf-8 -*-
from Crypto.Util.number import long_to_bytes
import requests
import re


class RSA_n:
    def __init__(self, n=None, c=None, e=None):
        self.n = int(n)
        self.c = int(c)
        self.e = int(e)

    '''辗转相除法'''
    def rsa_k(self, p, q):
        e1 = self.e
        n1 = (p - 1) * (q - 1)
        i = 0
        n2 = []
        e2 = []
        n2.append(n1)
        e2.append(self.e)
        while True:
            i += 1
            n1 = n1%e1
            n2.append(n1)
            if n1 == 1:
                if i == 1:
                    d1 = 1
                    k = (e1 * d1) - 1
                    break
                else:
                    '''d * e - n1 * k = 1'''
                    # 最后一步 k = e - 1
                    k = (e2[i-1] * 1 - 1) // n2[i]
                    for j in range(i-1):
                        d1 = (1 + (k * n2[i - j - 1])) // e2[i - j - 1]
                        k = (e2[i - (j + 1) - 1] * d1 - 1) // n2[i - j - 1]
                    break
            else:
                e1 = e1 % n1
                e2.append(e1)
                if e1 == 1:
                    if i == 1:
                        d1 = 1
                        k = (self.e * d1 -1) // n1
                        break
                    else:
                        # k=0,d1=1 最后一步
                        # 倒数第二步开始，往前求d
                        # K != 1
                        '''d * e - n1 * k = 1'''
                        k = (e2[i-1] * 1 -1) // n2[i]
                        for j in range(i-1):
                            d1 = (1 + (k*n2[i-j-1])) // e2[i-j-1]
                            k = (e2[i-(j+1)-1] * d1 -1) // n2[i-j-1]
                        break
        self.rsa_d(p,q,k)

    def rsa_d(self, p, q, k):
        n1 = (p - 1) * (q - 1)
        # 第一步
        d = (1 + n1 * int(k)) // self.e
        print("d =", d)
        self.rsd_m(int(d))

    def rsd_m(self, d):
        m = pow(self.c,d,self.n)
        print("m = ", m)
        flag = long_to_bytes(m)
        try:
            print('[+] 解密完成\n明文为：',flag.decode('utf-8'))
        except:
            print('[+] 解密完成\n明文为：',flag)

    def n_factoring(self):
        try:
            print("[+] 正在因式分解 n, 请稍后...")
            url = 'http://factordb.com/index.php?query='
            urls = url + str(self.n)
            result = requests.get(urls)
            re_p = re.findall('<a href="(.*?)"><font',result.text)[1]
            re_q = re.findall('<a href="(.*?)"><font',result.text)[2]
            url_p = 'http://factordb.com/' + re_p
            result_p = requests.get(url_p)
            p = re.findall('<input type="text" size=100 name="query" value="(\d*?)">',result_p.text)[0]
            url_q = 'http://factordb.com/' + re_q
            result_q = requests.get(url_q)
            q = re.findall('<input type="text" size=100 name="query" value="(\d*?)">', result_q.text)[0]
            print(f'''
[+] 因式分解完成
p = {p}
q = {q}
正在解密...
            ''')
            self.rsa_k(int(p),int(q))
        except:
            print("[-] 出错啦！请重新来！")

