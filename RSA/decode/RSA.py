'''
Function:
    RSA解密算法
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hscsec.cn
'''
# -*- coding:utf-8 -*-

class RSA:
    def __init__(self, n=None, c=None, e=None, p=None, q=None):
        self.n = int(n)
        self.c = int(c)
        self.e = int(e)
        self.p = int(p)
        self.q = int(q)

    def rsa_k(self):
        e1 = self.e
        n1 = (self.p - 1) * (self.q - 1)
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
                    k = (e2[i - 1] * 1 - 1) / n2[i]
                    for j in range(i - 1):
                        d1 = (1 + (k * n2[i - j - 1])) / e2[i - j - 1]
                        k = (e2[i - (j + 1) - 1] * d1 - 1) / n2[i - j - 1]
                    break
            else:
                e1 = e1 % n1
                e2.append(e1)
                if e1 == 1:
                    if i == 1:
                        d1 = 1
                        k = (self.e * d1 -1) / n1
                        break
                    else:
                        # k=0,d1=1 最后一步
                        # 倒数第二步开始，往前求d
                        '''d * e - n1 * k = 1'''
                        k = (e2[i-1] * 1 -1) / n2[i]
                        for j in range(i-1):
                            d1 = (1 + (k*n2[i-j-1])) / e2[i-j-1]
                            k = (e2[i-(j+1)-1] * d1 -1) / n2[i-j-1]
                        break
        self.rsa_d(k)

    def rsa_d(self, k):
        n1 = (self.p - 1) * (self.q - 1)
        # 第一步
        # " / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法
        d = (1 + n1 * int(k)) // self.e
        self.rsd_m(int(d))

    def rsd_m(self, d):
        from Crypto.Util.number import long_to_bytes
        m = pow(self.c,d,self.n)
        flag = long_to_bytes(m)
        try:
            print('[+] 解密完成\n明文为：',flag.decode('utf-8'))
        except:
            print('[+] 解密完成\n明文为：', flag)


