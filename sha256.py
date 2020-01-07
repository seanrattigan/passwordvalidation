import hashlib

# missing docstring
def hashpass(password):
	hash_thiss = hashlib.sha256((password).encode('utf-8')).hexdigest()
    # rather than print, return the hash
	print(f"Your password is : {hash_thiss}")