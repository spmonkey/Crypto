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
    from Crypto.Util.number import long_to_bytes
    m = pow(c,d,n)
    flag = long_to_bytes(m)
    print('flag =',flag.decode('utf-8'))

if __name__ == '__main__':
    p = input("请输入p:")
    q = input("请输入q:")
    e = input("请输入e:")
    n = input("请输入n:")
    c = input("请输入c:")
    rsa_k(int(p),int(q),int(e))

