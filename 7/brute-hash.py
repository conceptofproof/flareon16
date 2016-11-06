#!/usr/bin/python
from hashlib import *
from itertools import *

targets = ["3cab2465e955b78e1dc84ab2aad1773641ef6c29","4a1bf8bd1e91f3593a6ccc9cc9b2d5682e62244f","9e6061a36250e1c47e69f0312db4e561528a1fb5"]

charset = "abcdefghijklmnopqrstuvwxyz@-._1234"
for c in product(charset, repeat=6):
    test = ''.join(c)
    m = sha1()
    m.update(test)
    for i in range(2):
      b = m.digest()
      m = sha1()
      m.update(b)
    if m.hexdigest() in targets:
      print '[*] "'+test+'" matches '+m.hexdigest()
    

