# Mongo ORM implementation using pymongo

###### Example
```Python
>>> from mongodb import MongoDataRepository
>>> mydata = MongoDataRepository('test_repo')
>>> mydata.add_record({'id': 1, 'name':'Gopal Gautam', 'prof': 'Software Engineer'})
>>> mydata.add_record({'id': 2, 'name':'Shyam Koirala', 'prof': 'Civil Engineer'})
>>> mydata.count()
2
>>> mydata.update_or_create({'id': 1, 'name':'Raju Gautam', 'prof': 'Software Engineer' })
>>> mydata.count()
2
>>> a=mydata.find_record({'id':1})
>>> list(a)
[{'name': 'Raju Gautam', '_id': ObjectId('5ad5a837343fd94530bcb6a7'), 'prof': 'Software Engineer', 'id': 1}]
>>> mydata.delete_record(1)
>>> mydata.count()
1
>>> mydata.find_record({'id':1})
>>> list(mydata.find_record({'id':1}))
[]
>>> list(mydata.find_record({'name':'Raju Gautam'}))
[]
>>> list(mydata.find_record({'name':'Shyam Koirala'}))
[{'name': 'Shyam Koirala', '_id': ObjectId('5ad5a87a343fd94530bcb6a8'), 'prof': 'Civil Engineer', 'id': 2}]
```
