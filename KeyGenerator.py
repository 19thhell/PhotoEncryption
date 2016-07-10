import rsa

(pubkey, privkey) = rsa.newkeys(4096, poolsize=2)

with open('public_key.pem', 'wb') as pub_pem:
    pub_pem.write(pubkey.save_pkcs1())

with open('private_key.pem', 'wb') as priv_pem:
    priv_pem.write(privkey.save_pkcs1())
