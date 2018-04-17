# Mongo ORM implementation using pymongo

###### Example
```Python
from mongodb import MongoDataRepository
mydata = MongoDataRepository('test_repo')
mydata.add_record({'id': 1, 'name':'Gopal Gautam', 'prof': 'Software Engineer'})
mydata.add_record({'id': 2, 'name':'Shyam Koirala', 'prof': 'Civil Engineer'})
mydata.count()
2
mydata.update_or_create({'id': 1, 'name':'Raju Gautam', 'prof': 'Software Engineer' })
```
