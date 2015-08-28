#!/usr/bin/python
# This IDAPython code can be used to de-obfuscate strings generated by
# CryptoWall version 3, as well as any other malware samples that make use of
# this technique. 

'''
Example disassembly:

	.text:00403EC8                 mov     ecx, 'V'
	.text:00403ECD                 mov     [ebp+var_1C], cx
	.text:00403ED1                 mov     edx, 'e'
	.text:00403ED6                 mov     [ebp+var_1A], dx
	.text:00403EDA                 mov     eax, 'r'
	.text:00403EDF                 mov     [ebp+var_18], ax
	.text:00403EE3                 mov     ecx, 's'
	.text:00403EE8                 mov     [ebp+var_16], cx
	.text:00403EEC                 mov     edx, 'i'
	.text:00403EF1                 mov     [ebp+var_14], dx
	.text:00403EF5                 mov     eax, 'o'
	.text:00403EFA                 mov     [ebp+var_12], ax
	.text:00403EFE                 mov     ecx, 'n'
'''

pos = here()
original_pos = pos
out = ""
while True:
	if GetMnem(pos) == "mov" and GetOpnd(pos, 0)[0] == "e" and GetOpnd(pos, 0)[2] == "x":
		out += chr(GetOperandValue(pos,1))
	elif GetMnem(pos) == "mov" and "[ebp" in GetOpnd(pos, 0):
		None
	elif GetMnem(pos) == "xor":
		MakeComm(original_pos, out)
		print "Making String: %s" % out
		out = ""
		original_pos = pos
	else:
		break
	pos = NextHead(pos)



