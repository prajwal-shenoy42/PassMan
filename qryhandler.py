def insert_secret(cursor, connection, url, userid, password):
    query = "Insert into secret_storage(URL, userid, password) values (\'" + url + "\', \'" + userid + "\', \'" + password + "\');"
    cursor.execute(query)
    connection.commit()

def delete_secret(cursor, connection, url, userid):
    query = "Delete from secret_storage where url = \'" + url + "\' and userid = \'" + userid + "\';"
    cursor.execute(query)
    connection.commit()

def fetch_secret(cursor, url):
    query = "Select * from secret_storage where url = \'" + url + "\';"
    cursor.execute(query)
    print(cursor.fetchall())
