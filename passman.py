import psycopg2
import qryhandler

conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
cursor = conn.cursor()

qryhandler.fetch_secret(cursor, "google.com")

conn.close()