# AirBnB_clone
#0x00. AirBnB clone - The console
---
## This project will cover:
*How to create a Python package to do an AirBnB clone.

*How to create a command interpreter in Python using the cmd module

*What is Unit testing and how to implement it in a large project

*How to serialize and deserialize a Class

*How to write and read a JSON file

*How to manage datetime

*What is an UUID

*What is *args and how to use it

*What is **kwargs and how to use it

*How to handle named arguments in a function

This project will create a website and will create objects for the website. 

The console will be used to create/delete objects, update/add attributes etc. 

Each object will have a unique id and a time it was created.


## Description
Our console will display a prompt (hbnb).

The prompt will appear each time a command has been executed. 

If an executable cannot be found it will print an error. 

Handles EOF, quit as well as other built-in commands: 


## How to start our console
./console.py

## List of built in commands
*create - creates a new instance of a class.
*show - prints the string representation of an instance based in the class name
and id.
*destroy - deletes an instance based on the class and id. 
*all - Prints a string rep. of all instances based or not on the class name.
*update - updates an instance based on the class name and id by adding or
updating an attribute.

## Examples
To create a new instance of BaseModel:

(hbnb) create BaseModel

49faff9a-6318-451f-87b6-910505c55907

(hbnb) all Base

** class doesn't exist **

(hbnb) all BaseModel

["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

(hbnb) destroy BaseModel 

49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 

49faff9a-6318-451f-87b6-910505c55907

** no instance found **



File|Task
---|---
base_model.py | The Base class of all other classes
file_storage.py | The engine that stores all the objects
state.py | A state object
city.py | A city object
amenity.py | A amenities object
user.py | A User object
review.py | A Review object
place.py | A place object
console.py | A python console to manipulate objects in our project
