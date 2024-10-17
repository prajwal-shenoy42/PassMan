from argon2 import PasswordHasher
import generator as gen

ph = PasswordHasher()

def generate(pwd):
    salt = gen.generate("salt")
    salted_pwd = pwd + salt
    hashed_secret = ph.hash(salted_pwd)
    return [hashed_secret,salt]

def verify(hash, pwd):
    return ph.verify(hash, pwd)