#! /usr/bin/python
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto import Random

def enc(key,p):
	return ARC4.new(key).encrypt(p)

def dec(key,msg):
    return ARC4.new(key).decrypt(msg)

def main():
    print("\n")
    key = 'key for testing rc4'
    p = 'This is my First RC4 programming'
    print("key: "+key)

    print("\n")
    print("plain text: "+p)
    print("\n")
    nonce=Random.new().read(16)
    key += nonce
    key = SHA256.new(key).digest()
    #key is no more than 256bytes

    print ("Decrypted Msg: "+dec(key,enc(key,p)))

if __name__=='__main__':
		main()
