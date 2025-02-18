#!/bin/sh

service mysql start                      # start MySQL service

python3 init_db.py                       # initializes the MySQL database (not the tables, but just the DB)
                                         # and the user profile if they don't exist

python3 manage.py makemigrations         # for dev purposes, creates migration files for changes
python3 manage.py migrate                # applies migration to MySQL db

python3 createsuperuser.py               # makes admin account if it does not exist

python3 manage.py runserver 0.0.0.0:8000 # put on port 8000