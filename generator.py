import secrets
import string
   
def generate(value):
    punctuation = string.punctuation[0:6] + string.punctuation[7:23] + string.punctuation[24:]
    alphabet = string.ascii_letters + string.digits + punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    return password