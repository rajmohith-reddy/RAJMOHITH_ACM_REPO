ciphertext = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
)
known = b'crypto{'

for i in range(len(known)):
    k = ciphertext[i] ^ known[i]
    print(chr(k))

key = b'myXORkey'

for i in range(len(ciphertext)):
    k = key[i % len(key)]
    out = ciphertext[i] ^ k
    print(chr(out), end="") 

txt = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hint = b'crypto{'
for i in range(len(hint)):
	k = txt[i] ^ hint[i]
	print(chr(k))

for i in range(len(txt)):
	k = key[i % len(key)]
	out = ciphertext[i] ^ k
	print(chr(out), end="")