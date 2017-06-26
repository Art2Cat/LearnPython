#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import re

email = ['someone@gmail.com', 'test@art2cat.com', 'yy.tt@live.com',
         'test@bbc.co.uk', 'test@s-i-m.com']

re_email = re.compile(r'^([a-zA-Z0-9._]*)(\@)([a-z0-9\-_]*)([.a-z]*)$')

for i in email:
    print(re_email.match(i).groups())
