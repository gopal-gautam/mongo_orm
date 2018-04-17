from pymongo import MongoClient

def _getcondb(db_name):
    con = MongoClient()
    return con[db_name]

class MongoDataRepository(object):

    pk = 'id' #making id function like primary key in relational db
    def __init__(self, repo): #repo is my collection name
        self.db = _getcondb('repo_db')  #mongo database
        self.repo = self.db[repo]
        self.repo.create_index(self.pk, unique=True) #Creating index on pk and making it unique


    def count(self):
        return self.repo.count()

    def add_record(self, dictrecord):
        if isinstance(dictrecord, dict):
            # if dictrecord.has_key(self.pk): #Python 2
            if self.pk in dictrecord: #python 3
                return self.repo.insert_one(dictrecord)
            else:
                raise KeyError("Record should have {} key".format(self.pk))
        raise TypeError("Cant insert non-dictionary object")

    def find_record(self, query):
        return self.repo.find(query) #query should be in dict

    def update_record(self, pk, dictset):
        return self.repo.update_one(
            {self.pk: pk}, #search
            {'$set': dictset }, #update data
            upsert= False #making sure that existing data exist
        )

    def delete_record(self, pk):
        return self.repo.delete_one({self.pk: pk})

    def update_or_create(self, dictset):
        pk = dictset[self.pk]
        record = dictset.copy()
        if self.find_record({self.pk: pk}).count() == 1:
            del record[self.pk] #Dont want to update id
            return self.update_record(pk=pk, dictset=record)
        else:
            return self.add_record(dictrecord=record)

    def value_of_record_key(self, pk, key):
        record = self.find_record({self.pk: pk})
        for que in record:
            if key in que:
                return que[key]
        return ""











