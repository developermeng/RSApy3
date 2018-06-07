# coding=utf-8

import rsa,sys

# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

# 明文
message = '192.168.1.100:s7_1:start S7Pot'

# 公钥加密
crypto = rsa.encrypt(message.encode(), pubkey)

print(crypto)

print (type(crypto))

print (sys.getsizeof(crypto))

# 私钥解密
message = rsa.decrypt(crypto, privkey).decode()
print(message)
