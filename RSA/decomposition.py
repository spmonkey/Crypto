from math import sqrt

num = int("",16)
print(num)
# if num.isdigit():
#     num = int(num, 16)
# else:
#     print("输入非法，请输入一个合数")
#     exit()
#
# if num < 2:
#     print("请输入一个大于2的合数")
#     exit()

# 判断是否为质数
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

l_1 = []

# 分解质数
def decomposition(num):
    i = 2
    while i < num + 1:
        if num % i == 0:
            l_1.append(i)
            num = num / i
        else:
            i += 1

if not is_prime(num):
    decomposition(num)
    str_1 = ''
    for i in l_1:
        str_1 = str_1 + str(i) + "*"
    str_1 = str_1[:-1]
    print("%s=%s"%(num,str_1))
else:
    print("%s是一个质数，请输入合数"%num)

# from Crypto.PublicKey import RSA
# f = open("pubkey.pem", "r")
# key = RSA.importKey(f.read())
# print(key.n)
# print(key.e)