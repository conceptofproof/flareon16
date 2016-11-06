# Python bytecode 2.7 disassembled from Python 2.7
# Embedded file name: poc.py
import sys
import random

count = 1

for i in range(25):
  win_msg = 'Wahoo, you guessed it with %d guesses\n' % i

  tmp = '312a232f272e27313162322e372548'
  stuffs = [67,
  139,
  119,
  165,
  232,
  86,
  207,
  61,
  79,
  67,
  45,
  58,
  230,
  190,
  181,
  74,
  65,
  148,
  71,
  243,
  246,
  67,
  142,
  60,
  61,
  92,
  58,
  115,
  240,
  226,
  171]
  a = ""
  import hashlib
  stuffer = hashlib.md5(win_msg + tmp).digest()
  for x in range(len(stuffs)):
    a+=chr(stuffs[x] ^ ord(stuffer[x % len(stuffer)]))
  print a
