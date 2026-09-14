key = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

k = key[0] ^ ord("c")

print("Key:", k)

out = bytes(a ^ k for a in key)

print(out.decode())