from argon2 import PasswordHasher

ph = PasswordHasher()

def generate(pwd):
    hashed_secret = ph.hash(pwd)
    return hashed_secret

def verify(hash, pwd):
    return ph.verify(hash, pwd)