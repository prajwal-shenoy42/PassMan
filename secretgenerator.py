import secrets
import string
punctuation = string.punctuation[0:23] + string.punctuation[24:]
alphabet = string.ascii_letters + string.digits + punctuation
password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
print(password)