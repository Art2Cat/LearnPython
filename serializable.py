#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import json
import pickle

d = dict(name='Test', age=13, zipcode=12306)
print(pickle.dumps(d))

with open('test.txt', 'wb') as f:
    pickle.dump(d, f)

with open('test.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

print(json.dumps(d))

json_str = '{"name": "Test", "age": 13, "zipcode": 12306}'

print(json.loads(json_str))


class Test(object):
    def __init__(self, name, age, code):
        self.name = name
        self.code = code
        self.age = age


def test2dict(test):
    return {
        'name': test.name,
        'age': test.age,
        'code': test.code
    }


def dict2test(d):
    return Test(d['name'], d['age'], d['code'])


t = Test('Test', 25, 12036)
print(json.dumps(t, default=test2dict))

s = json.dumps(t, default=lambda obj: obj.__dict__)

print(json.loads(s, object_hook=dict2test))

reb = json.loads(s, object_hook=lambda d: Test(
    d['name'], d['age'], d['code']))

print(reb)
