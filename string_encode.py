#!/user/bin/env python
# coding:utf-8

ASCII = 'ascii'
UTF8 = 'utf-8'
UTF16 = 'utf-16'
GB2312 = 'gb2312'
GBK = 'gbk'
GB18030 = 'gb18030'
UNICODE = 'unicode'

print("我是不是中国人，显然不是才怪 apparently")

s = u"哈哈哈字符串"

x = s.encode(GBK)

x = x.decode(GBK)
print(x)
z = s.encode(UTF8)
print(z)

y = ord("A")
print(y)
print(chr(6616))

r = (85 - 72) / 72
print('%.2f %%' % r)

lists = []
for i in range(10):
    lists.insert(i, i)
print(lists)

lists.clear()
lists = [i for i in range(10)]

for i in range(10):
    lists.append(i)

print(lists)
print(lists[-3:])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
