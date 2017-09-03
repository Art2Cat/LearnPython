#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import re

email = ['someone@gmail.com', 'test@art2cat.com', 'yy.tt@live.com',
         'test@bbc.co.uk', 'test@s-i-m.com']

re_email = re.compile(r'([a-zA-Z0-9._]*)(\@)([a-z0-9\-_]*)([.a-z]*)')

for i in email:
    result = re_email.match(i)
    if result is not None:
        print(re_email.match(i).groups())


material = 'params.put("test", "required")'
result0 = re.search('([^required])', material)
if result0 is not None: 
    print(result0.groups())
    print(result0.group(1))