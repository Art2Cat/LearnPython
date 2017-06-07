#!/user/bin/env python3

ASCII = 'ascii'
UTF8 = 'utf-8'
UTF16 = 'utf-16'
GB2312 = 'gb2312'
GBK = 'gbk'
GB18030 = 'gb18030'
UNICODE = 'unicode'

print("我是不是中国人，显然不是才怪 apparently")

s = u"字符串"

x = s.encode(GBK)

x = x.decode(GBK)
print(x)
z = s.encode(UTF8)
print(z)

y = ord("A")
print(y)
print(chr(66))

r = (85 - 72) / 72
print('%.2f %%' % r)
