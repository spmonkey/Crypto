import binascii,gmpy2
from functools import reduce
import libnum

class RSA_wiener:
    def __init__(self, n=None, c=None, e=None):
        self.n = n
        self.c = c
        self.e = e

    def CRT(self):
        assert (reduce(gmpy2.gcd, self.n) == 1)
        assert (isinstance(self.n, list) and isinstance(self.c, list))
        M = reduce(lambda x, y: x * y, self.n)
        ai_ti_Mi = [a * (M // m) * gmpy2.invert(M // m, m) for (m, a) in zip(self.n, self.c)]
        text = reduce(lambda x, y: x + y, ai_ti_Mi) % M
        m = gmpy2.iroot(text, self.e)[0]
        print('[+] 解密完成\n明文为：',libnum.n2s(int(m)))

# if __name__ == "__main__":
#
#     m = CRT(n1, c1)
#     m1 = iroot(m, e)  # 开e次方
#     print(m1)
#     print(libnum.n2s(int(m1[0])))