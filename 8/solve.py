#!/usr/bin/python

grape = "38E14A1B0C1A46460A96297373A46903001BA8F8B82416D609CB"

banana = "FF157420400089EC5DC34246C063862AAB08BF8C4C25193192B0AD14A2B667DD39D85F3F7B5CC2B2F62E759B6194CFCE6A9850F25BF045300E38EB3B6C667F243DDF8897B9B3F1CB83991A0DEFB103559E9A7A10E036E8D3E432C17807B76BC770C92CA091356DFE735EF4A4D9DB4369F58DEE447D48B5DC4B02A1E3D2A6213E2FA3D7BB845AFB8F121C4128C576599CF73306270A0BAF71164AE99F4F6FE20FBE2BE756D553792D641795A7BD7C1D5893A565F81813EABCE5F3370496A81E012982513C681F8EDA8A05227249FA87A95462C6AA09B4FDD6D1AC8511473A9DE64D1BCC528023FCED8B7E60CD6E57BADEAECAC4770C4ED4D0C8E1B8F926908134" 

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

temp = []
solution = []

seed = int(grape[:2],16)^0xc5
temp.append(seed)
for i in range(1,26):
	temp.append(int(grape[(i-1)*2:((i-1)*2)+2],16)^int(grape[i*2:(i*2)+2],16))

seed = temp[25]^0xaf
solution.insert(0,chr(seed))

for i in range(24,-1,-1):
	index = rol(temp[i+1],3,8)
	index = int(banana[2*index:(2*index)+2],16)
	value = int(banana[2*index:(2*index)+2],16)
	solution.insert(0,chr(temp[i]^value))

print ''.join(solution)

