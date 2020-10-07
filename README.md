# contactAPI
---

### This is a basic API that is used to perform basic CRUD operations using MongoDB as a database.

To use this api first install dependencies by running the below command:-
```
pip install -r requirements.txt
```
and install mongoDB either by referring to its official website or by using below link
```
sudo apt-get install mongodb
```
Then verify the version of MongoDB and Flask to make sure everything is installed properly (should be latest) by using the following commands:-
```
mongo --version
flask --version
```
Then start mongoDB in a command line interface and create a database. (here i am going to use database named 'Contact', you can use any database name)
To start mongoDB in a command line interface type following command:-
```
mongo
```
then create database using the following command:-
```
use DATABASE_NAME
```
and close the terminal.


To run the api use the following command-
```
python run.py
```

This API contains the following routes -

1: /   - Here the whole index is displayed

2: /add   - It adds contacts in the database, you need to give name, email, mobile in json format as a 'POST' request

3: /searchByEmail   - It search contacts in the database by email, you need to give email in json format as a 'GET' request

4: /searchByName   - It search contacts in the database by name, you need to give name in json format as a 'GET' request

5: /update   - It update contacts info. in the database, you need to give name, email, mobile in json format as a 'PUT' request

6: /delete   - It delete contacts from the database, you need to give email in json format as a 'DELETE' request


#### I have tested this API using Postman. 
