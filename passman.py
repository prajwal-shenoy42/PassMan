import psycopg2
import qryhandler
import argparse

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
cursor = conn.cursor()

parser = argparse.ArgumentParser(description="ArgumentParser for Passman")
parser.add_argument("-a", "--add", help="add entry into passman", action="store_true")
parser.add_argument("-d", "--delete", help="remove entry from passman", action="store_true")
parser.add_argument("-f", "--fetch", help="fetch entry from passman", action="store_true")
parser.add_argument("-u", "--url", nargs=1, help="url of the website")
parser.add_argument("-n", "--username", nargs=1, help="username for the given url")


args = parser.parse_args()
if args.add:
    qryhandler.insert_secret(cursor, conn, args.url[0], args.username[0], "")
elif args.delete:
    qryhandler.delete_secret(cursor, conn, args.url[0], args.username[0])
elif args.fetch:
    qryhandler.fetch_secret(cursor, args.url[0])

conn.close()