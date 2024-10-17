import hashhandler as hh
import qryhandler as qh
import getpass

def create_user(cursor, connection, firstname, lastname, username):
    master_pwd = getpass.getpass(prompt='Enter a Master password for your user account: ')
    integrity_info = hh.generate(master_pwd)
    qh.create_user(cursor, connection, firstname, lastname, username, integrity_info[0], integrity_info[1])