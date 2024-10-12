#!/bin/bash
# https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
# !!! don't forget to add ; at end of statement
sudo -u postgres psql
postgres=# create database djangotraining;
postgres=# create user djangouser with encrypted password 'secret';
postgres=# grant all privileges on database mydb to djangouser;