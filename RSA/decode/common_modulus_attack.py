'''
Function:
    RSA共模攻击
Author:
    spmonkey
博客链接:
    https://www.cnblogs.com/spmonkey/
邮箱：
    spmonkey@hscsec.cn
Github:
    https://github.com/spmonkey/
'''
import gmpy2
import libnum

class common_modulus:
    def __init__(self, n=None, e1 = None, c1=None, e2=None, c2=None):
        self.n = int(n)
        self.e1 = int(e1)
        self.c1 = int(c1)
        self.e2 = int(e2)
        self.c2 = int(c2)

    def RSA_common_modulus_attack(self):
        print(f"e1 = {self.e1}\ne2 = {self.e2}")
        print("e1和e2的最大公约数：",gmpy2.gcd(self.e1, self.e2))
        s = gmpy2.gcdext(self.e1, self.e2)
        s1 = s[1]
        s2 = s[2]
        if s1 < 0:
            s1 = - s1
            c1 = gmpy2.invert(self.c1, self.n)
        elif s2 < 0:
            s2 = - s2
            c2 = gmpy2.invert(self.c2, self.n)
        m = (pow(c1, s1, self.n) * pow(c2, s2, self.n)) % self.n
        return int(m),libnum.n2s(int(m)).decode('utf-8')



