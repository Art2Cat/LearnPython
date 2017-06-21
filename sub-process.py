#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import subprocess

print('$ nslookup www.art2cat.com')
r = subprocess.call(['nslookup', 'www.art2cat.com'])
print('Exit code:', r)
