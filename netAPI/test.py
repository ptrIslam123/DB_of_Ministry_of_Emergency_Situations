#! /usr/bin/env python
#-*-coding: utf-8-*-


from itertools import izip_longest


def grouper(iterable, n, fillvalue=' '):
    iterable = iterable.decode('utf-8')
    args = [iter(iterable)] * n

    ans = list(izip_longest(fillvalue=fillvalue, *args))

    for i in range(len(ans)):
        ans[i] = "".join(ans[i])


    return ans




#s = "апапрпрп".decode('utf-8')
s = "abcdefg"
k = 3

res = grouper(s, k)

print(type(res))
for i in res:
    print("[{i}] {len_str}".format(i=i, len_str=len(i)))