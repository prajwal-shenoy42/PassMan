def insert_secret(cursor, connection, url_name, userid, password):
    query = "Insert into secret_storage(url_name, userid, password) values (\'" + url_name + "\', \'" + userid + "\', \'" + password + "\');"
    cursor.execute(query)
    connection.commit()

def delete_secret(cursor, connection, url_name, userid):
    query = "Delete from secret_storage where url_name = \'" + url_name + "\' and userid = \'" + userid + "\';"
    cursor.execute(query)
    connection.commit()

def fetch_secret(cursor, url_name):
    query = "Select * from secret_storage where url_name = \'" + url_name + "\';"
    cursor.execute(query)
    print(cursor.fetchall())
