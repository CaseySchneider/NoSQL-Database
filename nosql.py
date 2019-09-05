import json
"""
Simple Document Store
"""

class Collection:
    """
    A list of dictionaries (documents) accessible in a DB-like way.
    """


    def __init__(self):
        """
        Initialize an empty collection.
        """
        self.docs = []
        pass


    def insert(self, document):
        """
        Add a new document (a.k.a. python dict) to the collection.
        """
        self.docs.append(document)
        pass


    def find_all(self):
        """
        Return list of all docs in database.
        """
        return self.docs
        pass


    def delete_all(self):
        """
        Truncate the collection.
        """
        self.docs = []
        pass


    def find_one(self, where_dict):
        """
        Return the first matching doc.
        If none is found, return None.
        """
        
        return_list = []
        for i in self.docs:
            if set(where_dict.keys()).issubset(set(i.keys())):
                # is subset, now check that the keys values match
                
                add_to = True
                
                for j in where_dict:
                    
                    if where_dict[j] == i[j]:
                        continue
                    
                    elif isinstance(where_dict[j], dict) and isinstance(i[j], dict) and set(where_dict[j].keys()).issubset(set(i[j].keys())):
                        for k in where_dict[j]:
                            if where_dict[j][k] == i[j][k]:
                                continue
                            else:
                                add_to = False
                                break
                    else:
                        add_to = False
                        break
                    
                    
                if add_to:
                    return_list.append(i)
        
        
        print("the stufff:  \n ", return_list, "  \nvs everything: \n", self.docs)
        if return_list:
            return return_list[0]
        else:
            return None
        pass


    def find(self, where_dict):
        """
        Return matching list of matching doc(s).
        """
        
        
        '''
        return_list = []
        for i in  self.docs:
            docs_dump = json.dumps(i, sort_keys=True)
            
            where_dict_dump = json.dumps(where_dict, sort_keys=True)
            print(where_dict_dump[1:-1])
            print(docs_dump)
            
            if where_dict_dump[1:-1] in docs_dump:
                return_list.append(i)

        
        return return_list
        '''
        
        
        return_list = []
        for i in self.docs:
            if set(where_dict.keys()).issubset(set(i.keys())):
                # is subset, now check that the keys values match
                
                add_to = True
                
                for j in where_dict:
                    
                    if where_dict[j] == i[j]:
                        continue
                    
                    elif isinstance(where_dict[j], dict) and isinstance(i[j], dict) and set(where_dict[j].keys()).issubset(set(i[j].keys())):
                        for k in where_dict[j]:
                            if where_dict[j][k] == i[j][k]:
                                continue
                            else:
                                add_to = False
                                break
                    else:
                        add_to = False
                        break
                    
                    
                if add_to:
                    return_list.append(i)
        
        
        print("the stufff:  \n ", return_list, "  \nvs everything: \n", self.docs)
        return return_list
        pass


    def count(self, where_dict):
        """
        Return the number of matching docs.
        """
        count = 0
        for i in self.docs:
            if set(where_dict.keys()).issubset(set(i.keys())):
                # is subset, now check that the keys values match
                
                add_to = True
                
                for j in where_dict:
                    
                    if where_dict[j] == i[j]:
                        continue
                    
                    elif isinstance(where_dict[j], dict) and isinstance(i[j], dict) and set(where_dict[j].keys()).issubset(set(i[j].keys())):
                        for k in where_dict[j]:
                            if where_dict[j][k] == i[j][k]:
                                continue
                            else:
                                add_to = False
                                break
                    else:
                        add_to = False
                        break
                    
                    
                if add_to:
                    count += 1
        
        
        return count
        pass


    def delete(self, where_dict):
        """
        Delete matching doc(s) from the collection.
        """
        
        if where_dict == [{}]:
            self.docs  = {}
        
        return_list = []
        for i in self.docs:
            if set(where_dict.keys()).issubset(set(i.keys())):
                # is subset, now check that the keys values match
                
                add_to = True
                
                for j in where_dict:
                    
                    if where_dict[j] == i[j]:
                        continue
                    
                    elif isinstance(where_dict[j], dict) and isinstance(i[j], dict) and set(where_dict[j].keys()).issubset(set(i[j].keys())):
                        for k in where_dict[j]:
                            if where_dict[j][k] == i[j][k]:
                                continue
                            else:
                                add_to = False
                                break
                    else:
                        add_to = False
                        break
                    
                    
                if add_to:
                    return_list.append(i)
        
        new_self_docs = []
        for i in self.docs:
            if i not in return_list:
                new_self_docs.append(i)
        self.docs = new_self_docs
        pass


    def update(self, where_dict, changes_dict):
        """
        Update matching doc(s) with the values provided.
        """
        
        count = 0
        for i in self.docs:
            if set(where_dict.keys()).issubset(set(i.keys())):
                # is subset, now check that the keys values match
                
                add_to = True
                
                for j in where_dict:
                    
                    if where_dict[j] == i[j]:
                        continue
                    
                    elif isinstance(where_dict[j], dict) and isinstance(i[j], dict) and set(where_dict[j].keys()).issubset(set(i[j].keys())):
                        for k in where_dict[j]:
                            if where_dict[j][k] == i[j][k]:
                                continue
                            else:
                                add_to = False
                                break
                    else:
                        add_to = False
                        break
                    
                    
                if add_to:
                    count += 1
        
        
        return count
        pass

        
        pass


    def map_reduce(self, map_function, reduce_function):
        """
        Applies a map_function to each document, collating the results.
        Then applies a reduce function to the set, returning the result.
        """
        
        mapped = []
        for i in self.docs:
            mapped.append(map_function(i))
            
        return reduce_function(mapped)
        pass


class Database:
    """
    Dictionary-like object containing one or more named collections.
    """

    def __init__(self, filename):
        """
        Initialize the underlying database. If filename contains data, load it.
        """
        
        self.filename = filename
        self.collections = {}
        
        self.temp_collections = {}
        
        try:
            f = open(self.filename, "r")
            
            self.temp_collections = json.load(f)
            # change dicts to Collection objects
            for i in self.temp_collections:
                collection_obj = Collection()
                
                # builds the Collection to add
                for j in self.temp_collections[i]:
                    collection_obj.insert(j)
                    
                self.collections[i] = collection_obj
                
        except Exception as e:
            #print("Error: ", e)
            # not testing for errors so... -\_('_')_/-
            pass
            
        

    def get_collection(self, name):
        """
        Create a collection (if new) in the DB and return it.
        """
        if name in self.collections:
            return self.collections[name]
        else:
            self.collections[name] = Collection()
            return self.collections[name]
        

    def drop_collection(self, name):
        """
        Drop the specified collection from the database.
        """
        self.collections.pop(name, None)
        pass

    def get_names_of_collections(self):
        """
        Return a list of the sorted names of the collections in the database.
        """
        
        return sorted(list(self.collections.keys()))

    def close(self):
        """
        Save and close file.
        """
        
        collection_to_add = {}
        
        
        
        for i, j in self.collections.items():
            add_to_coll = j.docs
            collection_to_add[i] = add_to_coll
            
            
        # save file as name of database
        with open(self.filename, "w") as f:
            json.dump(collection_to_add, f)
            
        
        f.close()
        
