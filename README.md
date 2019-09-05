# NoSQL-Database
A python implementation of a NoSQL database

Description
NoSQL-style databases are not characterized by any particular property, except that they have different goals than traditional SQL databases. For this project, you will be implementing a Document Store, a type of database with no schema, but can be useful none the less.

Files in Project6
project.py: This is the file you must implement the project. You are welcome to import other modules (both builtin and other custom files) for use in this file. Within, you must create two classes, "Collection" and "Database". It should contain your name, MSU email, feedback, and any sources beyond this course you used.
What you need to do
All of the code for this project could be placed in the "project.py" file.

Collection.__init__(self): This method initializes a collection.
Collection.insert(self, document): This method takes a document (a python dictionary) and adds it to the collection. The collection needs to store its documents in insertion order.
Collection.find_all(self): This method returns a list of all the documents stored in the collection in insertion order.
Collection.delete_all(self): This method removes all the documents stored in the collection.
Collection.find_one(self, where_dict):
This method returns the first document (in insertion order), that matches the where_dict. The where_dict is a python dictionary that contains key-value entries. If no match is found, return None.
If a document doesn't have each key in the where_dict, it doesn't match. If a document has the correct keys, but doesn't have the same associated values, it doesn't match.
If a where_dict is empty ({}), it matches all the documents.
Example: documents = {'age':27, 'name':'Josh', 'major':'CSE'}, where_dict = {'age':27, 'major':'CSE'}, the document matches because it has all the entries in the where clause. If the document was:{'age':27, 'name':'Tyler', 'major':'Street'}, it wouldn't match. This document also doesn't match: {'name':'Grant', 'major':'CSE'}.
Collection.find(self, where_dict):
This method returns the all the documents which match the where_dict (in insertion order). If no match is found, return an empty list.
Collection.count(self, where_dict):
This method returns the number of documents that match the where_dict.
Collection.delete(self, where_dict):
This method removes the documents that match the where_dict.
Collection.update(self, where_dict, changes_dict):
This method adds/updates the documents that match the where_dict with the changes_dict.
Collection.map_reduce(self, map_function, reduce_function):
This method takes two arguments which are both functions ("map_function" and "reduce_function"). It applies the map function to each document, saving the each's result to a list. This list is passed to the reduce function. The result of the reduce function is returned.
The map function will be provided by the test. Example:
def find_age(doc):
     if 'age' in doc:
          return doc['age']
     return 0
Example reduce function: sum (the builtin sum function returns the sum of all the values in a list).
Example documents [{'age':4}, {'name':'Jim', 'age': 2}, {'happy':'go lucky'}]
The result of calling map_reduce with the provided data is 6.
Database.__init__(self, filename): The init method for the Database class. It takes a filename that is where the database will store its information.
Database.get_collection(self, name): Returns a Collection instance associated with the given name. If no such Collection exists, create an empty one and return it. Otherwise return the Collection associated with the name. Note: the returned Collection shouldn't be a copy. Changes made to the Collection should be reflected in the database.
Database.get_names_of_collections(self): Returns a list of (sorted) names of collections in the Database.
Database.drop_collection(self, name): Removes the collection associated with the given name from the Database.
Database.close(self):
Saves the information in the Database to the file designated in the init method.
You can use whatever data format you want (JSON, XML, custom).
Then closes the database. This method will be called after working with the database.
After the close method is called, the Database will not be used again.
If a new Database is created using the same filename as a previously now closed Database, it should have the import the data and act like the original Database.
There can exist multiple, concurrent Database instances, but they will always have different filenames.
Tips
The tests for this project import and run your code. If your code outputs (prints) additional material, it will fail the test. I recommend a "debug_mode" global variable that you can use to test if you want to print additional messages for debugging purposes.

You should consider trying to solve the tests by hand before implementing the project.
