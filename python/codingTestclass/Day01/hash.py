import hashlib

def sha1_hash(input_string):
    hash_object = hashlib.sha1(input_string.encode())
    hash_value = hash_object.hexdigest()
    return hash_value

hash_value = sha1_hash("남영준")
print(hash_value, ", 길이 : ", len(hash_value))

hash_value2 = sha1_hash("1234")
print(hash_value2, ", 길이 : ", len(hash_value2))