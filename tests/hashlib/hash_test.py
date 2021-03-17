import hashlib

filename = r"D:\Data\testdata\djvu\Vas2.djvu"

file = open(filename, "rb")
hasher_md5 = hashlib.md5()
hasher_sha3_512 = hashlib.sha3_512()
hasher_sha3_256 = hashlib.sha3_256()
hasher_sha1 = hashlib.sha1()

buf = file.read()
hasher_md5.update(buf)
hasher_sha3_512.update(buf)
hasher_sha3_256.update(buf)
hasher_sha1.update(buf)

print("md5=", hasher_md5.hexdigest())
print("sha3_512=", hasher_sha3_512.hexdigest())
print("sha3_256=", hasher_sha3_256.hexdigest())
print("sha1=", hasher_sha1.hexdigest())


file.close()