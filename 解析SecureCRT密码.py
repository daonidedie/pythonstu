from Crypto.Cipher import Blowfish

#from Crypto.Cipher import Blowfish


def decrypt(password) :
    c1 = Blowfish.new('5F B0 45 A2 94 17 D9 16 C6 C6 A2 FF 06 41 82 B7'.replace(' ','').decode('hex'), Blowfish.MODE_CBC, '\x00'*8)
    c2 = Blowfish.new('24 A6 3D DE 5B D3 B3 82 9C 7E 06 F4 08 16 AA 07'.replace(' ','').decode('hex'), Blowfish.MODE_CBC, '\x00'*8)
    padded = c1.decrypt(c2.decrypt(password.decode('hex'))[4:-4])
    p = ''
    while padded[:2] != '\x00\x00' :
        p += padded[:2]
        padded = padded[2:]
    return p.decode('UTF-16')

#u558afae0ab392eb815d27bd47d0b2537de73b8c865717fb3d745ba9046b1e735
#print decrypt("xxx240f919a7a477198d1f6ce3a1fbf5a3671c82483f34bed1304c7ebe8de345");
print "PWD:"+ decrypt("558afae0ab392eb815d27bd47d0b2537de73b8c865717fb3d745ba9046b1e735");