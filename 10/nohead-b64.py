import glob
import base64
from tempfile import *
from subprocess import *
from time import sleep

def deleteContent(fName):
  with open(fName, "w"):
    pass

x = glob.glob('raw_bins/binaryData/*.bin')

count = 9
for i in x:
  count+=1
  print i
  f = open(i,'r')
  t = open('tempb64'+str(count),'wb+')
  d = open(i+"-nohead",'wb+')
  f.seek(16)
  for j in f:
    t.write(j)
  t.seek(0)
  d.write(base64.b64encode(t.read()))
