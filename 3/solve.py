#!/usr/bin/python


weirdarray = [0xee613e2f, 0xde79eb45, 0xaf1b2f3d, 0x8747bbd7, 0x739ac49c, 0xc9a4f5ae, 0x4632c5c1, 0xa0029b24, 0xd6165059, 0xa6b79451, 0xe79d23ba, 0x8aae92ce, 0x85991a18, 0xfee05899, 0x430c7994, 0x1ab9f36f, 0x70c42481, 0x05bd27cf, 0xc4ff6e6f, 0x5a77847c, 0xdd9277b3, 0x25843cff, 0x5fdca944, 0x8ee42896, 0x2ae961c7, 0xa77731da]


def mutate(x):
  i = 0
  for a in x:
    i = ord(a)+(0x25*i)
  return (i&0xffffffff)

def do_task():
  solution = ""
  j = 96 #'`' character
  for target in weirdarray:
    for i in range(32, 126):
      x = chr(i)+chr(j)+"FLARE On!"
      result = mutate(x)
      #print chr(i)+": "+str(hex(result))
      if result == target:
        solution += chr(i)
        j+=1

  print solution

if __name__ == '__main__':
	do_task() 

