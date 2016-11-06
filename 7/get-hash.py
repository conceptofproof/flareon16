from idaapi import *
from operator import *

i = 0x804bfd0 
hash = ""
while len(hash.translate(None,'\n'))<200:
  if i < 0x804bb80:
    i = 0x804cb80-(0x804bb80-i)
  #print hex(idc.Byte(i))
  hash = hex(idc.Byte(i))[2:].zfill(2)+hash
  if len(hash.translate(None,'\n'))%40==0:
    hash = "\n"+hash
  i-= 0x1cd
print hash 
