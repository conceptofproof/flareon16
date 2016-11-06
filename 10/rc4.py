import base64

with open("class_36-nohead-b64.bin", "r") as encrypted_file:
    data = base64.b64decode(encrypted_file.read())
key = "244a7ebe96927538dcdf5a3d6ea96cca"

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
with open('class_36-nohead-decrypted.txt', 'w') as decrypted_file:
    decrypted_file.write(decrypted_text)
