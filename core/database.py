import sqlite3
import os

# Paths to database file held in data
db_path = "data/SafePass_database.db"

# if file exists in db_path, creates connection to that file
def get_connection():
    return sqlite3.connect(db_path)

# if file doesn't exist in db_path, create a new database
def initialise_database():

    # create database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # table for master_password
    c.execute(""" 
    CREATE TABLE IF NOT EXISTS master_password(
    master_id INTEGER PRIMARY KEY,
    master_password TEXT);
    """) 

    # table for password_vault
    c.execute("""
    CREATE TABLE IF NOT EXISTS password_vault(
    entry_id INTEGER PRIMARY KEY,
    master_id INTEGER,
    website TEXT,
    username TEXT,
    password TEXT,
    FOREIGN KEY (master_id) REFERENCES master_password(master_id));
    """)