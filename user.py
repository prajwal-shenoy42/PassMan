import hashhandler as hh
import qryhandler as qh
import getpass

def create(cursor, connection, firstname, lastname, username):
    master_pwd = getpass.getpass(prompt='Enter a Master password for your user account: ')
    hash_val = hh.generate(master_pwd)
    qh.create_user(cursor, connection, firstname, lastname, username, hash_val)

def exists(cursor, username):
    if(qh.user_count(cursor, username) > 0):
        return True
    else:
        return False

def verify(cursor, username):
    user_exists = exists(cursor, username)
    if(user_exists):
        master_pwd = getpass.getpass(prompt='Please enter your Master Password: ')
        existing_hash = qh.retrieve_hash(cursor, username)
        try:
            if(hh.verify(existing_hash, master_pwd)):
                print("User verified")
                return True
            else:
                raise Exception("Incorrect Master Password")
        except Exception as e:
            print(e)
    else:
        print("User does not exist")