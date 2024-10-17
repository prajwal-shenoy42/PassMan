-- passman database
-- This is the database that will contain all the below tables
create database passman owner postgres;

-- master_info
-- This table stores the master password in hashed format and the salt used

create table master_info (
    username varchar(50) not null,
    hashed_secret varchar(100) not null,
    salt_value varchar(10) not null,
    primary key (username)
);

-- user_details
-- This table stores info about the users

create table user_details (
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    username varchar(50) not null references master_info (username),
    primary key (first_name, last_name)
);

-- secret_storage
-- This table is used to store all the passwords of a particular user for the different accounts on various websites
create table secret_storage (
    username varchar(50) not null references master_info (username),
    url_name varchar(100) not null,
    userid varchar(50) not null,
    password varchar(30) not null,
    primary key (username, url_name, userid)
);