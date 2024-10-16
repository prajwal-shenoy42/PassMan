import secrets
import string
   
def generate(value):
    punctuation = string.punctuation[0:6] + string.punctuation[7:23] + string.punctuation[24:]
    alphabet = string.ascii_letters + string.digits + punctuation
    if(value == "password"):
        password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
        return password
    elif(value == "salt"):
        salt = ''.join(secrets.choice(alphabet) for i in range(10))  # for a 10-character salt
        return salt