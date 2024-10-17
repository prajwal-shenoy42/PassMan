import hashhandler as hh
import qryhandler as qh
import getpass

def create(cursor, connection, firstname, lastname, username):
    master_pwd = getpass.getpass(prompt='Enter a Master password for your user account: ')
    integrity_info = hh.generate(master_pwd)
    qh.create_user(cursor, connection, firstname, lastname, username, integrity_info[0], integrity_info[1])

def exists(cursor, username):
    if(qh.user_count(cursor, username) > 0):
        return True
    else:
        return False

def verify(cursor, username):
    user_exists = exists(cursor, username)
    if(user_exists):
        master_pwd = getpass.getpass(prompt='Please enter your Master Password: ')
        salt = qh.retrieve_salt(cursor, username)
        salted_pwd = master_pwd + salt
        existing_hash = qh.retrieve_hash(cursor, username)
        try:
            if(hh.verify(existing_hash, salted_pwd)):
                print("User verified")
                return True
            else:
                raise Exception("Incorrect Master Password")
        except Exception as e:
            print(e)
    else:
        print("User does not exist")