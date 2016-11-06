#!/usr/bin/python
import md5
import base64

def rc4(target, md5hash):
  with open(target, "r") as encrypted_file:
    data = base64.b64decode(encrypted_file.read())
  key = md5hash

  S = range(256)
  j = 0
  out = []

  #KSA Phase
  for i in range(256):
      j = (j + S[i] + ord( key[i % len(key)] )) % 256
      S[i] , S[j] = S[j] , S[i]

  #PRGA Phase
  i = j = 0
  for char in data:
      i = ( i + 1 ) % 256
      j = ( j + S[i] ) % 256
      S[i] , S[j] = S[j] , S[i]
      out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

  decrypted_text = ''.join(out)
  with open(target+"-decrypted", 'w') as decrypted_file:
      decrypted_file.write(decrypted_text)
  return decrypted_text

def frighteningIntoxicant(array, pairs, result):
  a = pairs.split(",")
  for i in a:
    b = i.split(":")
    result.write(array[int(b[0])][int(b[1])])


order = [36,37,38,39,45,47,49,51,53,54,40,44,43,42,41,52,50,48,46,55,6,5,10,9,8,7,14,13,12,11,17,16,15,21,20,19,18,24,23,22,29,28,27,26,33,32,31,30,35,34,25]

# step 1: get first 16 bytes from raw binary
# step 2: "1BR0K3NCRYPT0FTW" + step 1
# step 3: md5(step 2)
# step 4: rc4(b64-encoded-bin-nohead, step3)
# step 5: push result onto marray[] 

marray = []
result = open("result.bin",'r+')

for i in order: 
  test = open('raw_bins/binaryData/class_'+str(i)+'.bin','r+')
  
  m = md5.new()
  m.update("1BR0K3NCRYPT0FTW"+test.read()[:16])  # combine key w/first 16 bytes of bin 
  md5hash =  m.digest().encode("hex")            # md5 hash the new string
  plaintext = rc4('raw_bins/b64/class_'+str(i)+'.bin-nohead', md5hash) # calculate 
  marray.append(plaintext)

p = open("pairs","r")
pairs = p.read()

frighteningIntoxicant(marray, pairs, result)

