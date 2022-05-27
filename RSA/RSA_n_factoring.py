'''
Function:
    RSA解密算法
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hsc2019.site
'''
# -*- coding:utf-8 -*-
from Crypto.Util.number import long_to_bytes
import requests, re

def rsa_k(p,q,e):
    e1 = e
    n1 = (p - 1) * (q - 1)
    i = 0
    n2 = []
    e2 = []
    n2.append(n1)
    e2.append(e)
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
            e1 = e1 % n1
            e2.append(e1)
            if e1 == 1:
                if i == 1:
                    d1 = 1
                    k = (e * d1 -1) / n1
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
    rsa_d(p,q,e,k)

def rsa_d(p,q,e,k):
    n1 = (p - 1) * (q - 1)
    # 第一步
    # " / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法
    d = (1 + n1 * int(k)) // e
    rsd_m(int(c),int(d),int(n))

def rsd_m(c,d,n):
    m = pow(c,d,n)
    flag = long_to_bytes(m)
    print('[+] 解密完成\nflag =',flag.decode('utf-8'))

def n_factoring(n):
    print("[+] 正在因式分解 n, 请稍后...")
    url = 'http://factordb.com/index.php?query='
    urls = url + str(n)
    result = requests.get(urls)
    re_p = re.findall('<a href="(.*?)"><font',result.text)[1]
    re_q = re.findall('<a href="(.*?)"><font',result.text)[2]
    url_p = 'http://factordb.com/' + re_p
    result_p = requests.get(url_p)
    p = re.findall('<input type="text" size=100 name="query" value="(\d*?)">',result_p.text)[0]
    url_q = 'http://factordb.com/' + re_q
    result_q = requests.get(url_q)
    q = re.findall('<input type="text" size=100 name="query" value="(\d*?)">', result_q.text)[0]
    print("[+] 因式分解完成，正在解密...")
    rsa_k(int(p),int(q),int(e))

if __name__ == '__main__':
    e = input("请输入e:")
    n = input("请输入n:")
    c = input("请输入c:")
    n_factoring(n)

