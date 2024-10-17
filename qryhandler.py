def insert_secret(cursor, connection, username, url_name, userid, password):
    query = "Insert into secret_storage(username, url_name, userid, password) values (\'" + username + "\', \'" + url_name + "\', \'" + userid + "\', \'" + password + "\');"
    cursor.execute(query)
    connection.commit()

def delete_secret(cursor, connection, username, url_name, userid):
    query = "Delete from secret_storage where username = \'" + username + "\' and url_name = \'" + url_name + "\' and userid = \'" + userid + "\';"
    cursor.execute(query)
    connection.commit()

def fetch_secret(cursor, username, url_name):
    query = "Select * from secret_storage where username = \'" + username + "\' and url_name = \'" + url_name + "\';"
    cursor.execute(query)
    print(cursor.fetchall())

def create_user(cursor, connection, firstname, lastname, username, hashed_secret, salt_value):
    query1 = "Insert into master_info(username, hashed_secret, salt_value) values (\'" + username + "\', \'" + hashed_secret + "\', \'" + salt_value + "\');"
    query2 = "Insert into user_details(first_name, last_name, username) values (\'" + firstname + "\', \'" + lastname + "\', \'" + username + "\');"
    cursor.execute(query1)
    cursor.execute(query2)
    connection.commit()

# store_hash function does not exist as hash of the master password is created and stored on creation of the user
def retrieve_hash():
    pass