import sys

x = 0x01020304

print(x.to_bytes(4, byteorder='big'))
print(x.to_bytes(4, byteorder='little'))

print(sys.byteorder)

print(int.from_bytes(b'\x04\x03\x02\x01', byteorder='big'))
print(int.from_bytes(b'\x04\x03\x02\x01', byteorder='little'))
