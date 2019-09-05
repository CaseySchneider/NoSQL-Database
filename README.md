# NoSQL-Database
A python implementation of a NoSQL database
<h2>Description</h2>
<p>NoSQL-style databases are not characterized by any particular property, except that they have different goals than traditional SQL databases. For this project, you will be implementing a Document Store, a type of database with no schema, but can be useful none the less.</p>
<h2>Files in Project6</h2>
<ul>
<li>project.py: This is the file you must implement the project. You are welcome to import other modules (both builtin and other custom files) for use in this file. Within, you must create two classes, "Collection" and "Database". It should contain your name, MSU email, feedback, and any sources beyond this course you used.</li>
</ul>
<h2>What you need to do</h2>
<p>All of the code for this project could be placed in the "project.py" file.</p>
<ul>
<li>
<code>Collection.__init__(self):</code>&nbsp;This method initializes a collection.</li>
<li>
<code>Collection.insert(self, document):</code>&nbsp;This method takes a document (a python dictionary) and adds it to the collection. The collection needs to store its documents in insertion order.</li>
<li>
<code>Collection.find_all(self):</code>&nbsp;This method returns a list of all the documents stored in the collection in insertion order.</li>
<li>
<code>Collection.delete_all(self):</code>&nbsp;This method removes all the documents stored in the collection.</li>
<li>
<code>Collection.find_one(self, where_dict):</code>
<ul>
<li>This method returns the first document (in insertion order), that matches the where_dict. The where_dict is a python dictionary that contains key-value entries. If no match is found, return None.</li>
<li>If a document doesn't have each key in the where_dict, it doesn't match. If a document has the correct keys, but doesn't have the same associated values, it doesn't match.</li>
<li>If a where_dict is empty ({}), it matches all the documents.</li>
<li>Example:&nbsp;<code>documents = {'age':27, 'name':'Josh', 'major':'CSE'}</code>,&nbsp;<code>where_dict = {'age':27, 'major':'CSE'}</code>, the document matches because it has all the entries in the where clause. If the document was:<code>{'age':27, 'name':'Tyler', 'major':'Street'}</code>, it wouldn't match. This document also doesn't match:&nbsp;<code>{'name':'Grant', 'major':'CSE'}</code>.</li>
</ul>
</li>
<li>
<code>Collection.find(self, where_dict):</code>
<ul>
<li>This method returns the all the documents which match the where_dict (in insertion order). If no match is found, return an empty list.</li>
</ul>
</li>
<li>
<code>Collection.count(self, where_dict):</code>
<ul>
<li>This method returns the number of documents that match the where_dict.</li>
</ul>
</li>
<li>
<code>Collection.delete(self, where_dict):</code>
<ul>
<li>This method removes the documents that match the where_dict.</li>
</ul>
</li>
<li>
<code>Collection.update(self, where_dict, changes_dict):</code>
<ul>
<li>This method adds/updates the documents that match the where_dict with the changes_dict.</li>
</ul>
</li>
<li>
<code>Collection.map_reduce(self, map_function, reduce_function):</code>
<ul>
<li>This method takes two arguments which are both functions ("map_function" and "reduce_function"). It applies the map function to each document, saving the each's result to a list. This list is passed to the reduce function. The result of the reduce function is returned.</li>
<li>The map function will be provided by the test. Example:
<pre>def find_age(doc):
     if 'age' in doc:
          return doc['age']
     return 0
</pre>
</li>
<li>Example reduce function:&nbsp;<code>sum</code>&nbsp;(the builtin sum function returns the sum of all the values in a list).</li>
<li>Example documents&nbsp;<code>[{'age':4}, {'name':'Jim', 'age': 2}, {'happy':'go lucky'}]</code>
</li>
<li>The result of calling map_reduce with the provided data is 6.</li>
</ul>
</li>
<li>
<code>Database.__init__(self, filename):</code>&nbsp;The init method for the Database class. It takes a filename that is where the database will store its information.</li>
<li>
<code>Database.get_collection(self, name):</code>&nbsp;Returns a Collection instance associated with the given name. If no such Collection exists, create an empty one and return it. Otherwise return the Collection associated with the name. Note: the returned Collection shouldn't be a copy. Changes made to the Collection should be reflected in the database.</li>
<li>
<code>Database.get_names_of_collections(self):</code>&nbsp;Returns a list of (sorted) names of collections in the Database.</li>
<li>
<code>Database.drop_collection(self, name):&nbsp;</code>Removes the collection associated with the given name from the Database.</li>
<li>
<code>Database.close(self):</code>
<ul>
<li>Saves the information in the Database to the file designated in the init method.</li>
<li>You can use whatever data format you want (JSON, XML, custom).</li>
<li>Then closes the database. This method will be called after working with the database.</li>
<li>After the close method is called, the Database will not be used again.</li>
<li>If a new Database is created using the same filename as a previously now closed Database, it should have the import the data and act like the original Database.</li>
<li>There can exist multiple, concurrent Database instances, but they will always have different filenames.</li>
</ul>
</li>
</ul>
<h2>Tips</h2>
<p>The tests for this project import and run your code. If your code outputs (prints) additional material, it will fail the test. I recommend a "debug_mode" global variable that you can use to test if you want to print additional messages for debugging purposes.</p>
<p>You should consider trying to solve the tests by hand before implementing the project.</p>
