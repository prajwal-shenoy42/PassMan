import psycopg2
import qryhandler as qh
import argparse
import generator as gen
import user

conn = psycopg2.connect(database="passman", user="postgres", password="postgres", host="localhost", port=5432)
cursor = conn.cursor()

parser = argparse.ArgumentParser(description="ArgumentParser for Passman")

# Action to be performed: Addition, Deletion or Fetching
parser.add_argument("-a", "--add", help="add entry into passman", action="store_true")
parser.add_argument("-d", "--delete", help="remove entry from passman", action="store_true")
parser.add_argument("-f", "--fetch", help="fetch entry from passman", action="store_true")

# Website URL and UserID for that website. Password is generated and stored automatically.
parser.add_argument("-u", "--url_name", nargs=1, help="url of the website")
parser.add_argument("-i", "--userid", nargs=1, help="userid for the given url")

# Flags for new user creation
parser.add_argument("-C", "--createuser", help="create a new user", action="store_true")
parser.add_argument("-F", "--firstname", nargs=1, help="firstname of the user")
parser.add_argument("-L", "--lastname", nargs=1, help="lastname of the user")
parser.add_argument("-U", "--username", nargs=1, help="the users username on passman")

args = parser.parse_args()
if args.createuser:
    user.create(cursor, conn, args.firstname[0], args.lastname[0], args.username[0])
elif args.add:
    is_user_verified = user.verify(cursor, args.username[0])
    if(is_user_verified):
        pwd = gen.generate("password")
        qh.insert_secret(cursor, conn, args.username[0], args.url_name[0], args.userid[0], pwd)
elif args.delete:
    is_user_verified = user.verify(cursor, args.username[0])
    if(is_user_verified):
        qh.delete_secret(cursor, conn, args.username[0], args.url_name[0], args.userid[0])
elif args.fetch:
    is_user_verified = user.verify(cursor, args.username[0])
    if(is_user_verified):
        qh.fetch_secret(cursor, args.username[0], args.url_name[0])
    # If userid is given then only 1 value should be returned. If not, all values for that URL should be returned.

conn.close()