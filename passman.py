import psycopg2
import qryhandler
import argparse
import generator as gen

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
cursor = conn.cursor()

parser = argparse.ArgumentParser(description="ArgumentParser for Passman")
parser.add_argument("-a", "--add", help="add entry into passman", action="store_true")
parser.add_argument("-d", "--delete", help="remove entry from passman", action="store_true")
parser.add_argument("-f", "--fetch", help="fetch entry from passman", action="store_true")
parser.add_argument("-u", "--url_name", nargs=1, help="url of the website")
parser.add_argument("-n", "--userid", nargs=1, help="userid for the given url")
parser.add_argument("-M", "--master", nargs=1, help="Master Password of the user")

args = parser.parse_args()
if args.add:
    pwd = gen.generate(value="password")
    qryhandler.insert_secret(cursor, conn, args.url_name[0], args.userid[0], pwd)
elif args.delete:
    qryhandler.delete_secret(cursor, conn, args.url_name[0], args.userid[0])
elif args.fetch:
    qryhandler.fetch_secret(cursor, args.url_name[0])
    # If userid is given then only 1 value should be returned. If not, all values for that URL should be returned.

conn.close()