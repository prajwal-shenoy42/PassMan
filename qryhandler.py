def insert_secret(cursor, connection, url, username, password):
    query = "Insert into secret_storage(URL, username, password) values (\'" + url + "\', \'" + username + "\', \'" + password + "\');"
    cursor.execute(query)
    connection.commit()

def delete_secret(cursor, connection, url, username):
    query = "Delete from secret_storage where url = \'" + url + "\' and username = \'" + username + "\';"
    cursor.execute(query)
    connection.commit()

def fetch_secret(cursor, url):
    query = "Select * from secret_storage where url = \'" + url + "\';"
    cursor.execute(query)
    print(cursor.fetchall())
