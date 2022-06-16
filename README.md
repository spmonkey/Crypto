# RSA 解密算法
    通过本人两天对RSA加密原理的研究以及一些解密逆运算的研究，写出该RSA解密算法，不过限制条件较多，往后会继续优化。
# 限制条件
    RSA.py 必须知道 p、q、n、e、c 才可使用本算法
    RSA_n_factoring.py 只需要知道 n、e、c 即可，且要求 p、q 是未知的
# 使用方法
    usage : python {0} -n {1} -e {1} -c {2}
        -n    两个不同的大素数的乘积 n.
        -e    加密钥 e.
        -c    密文 c.
# 安装模块库
    pip install pycryptodome
# 免责声明
    本脚本只用于参考学习，一切用于违法，犯罪与本人无关，网络不是法外之地
