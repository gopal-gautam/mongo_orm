# Mongo ORM implementation using pymongo

###### Example
```
from mongodb import MongoDataRepository
mydata = MongoDataRepository('test_repo')
mydata.add_record({'id': 1, 'name':'Gopal Gautam', 'prof': 'Software Engineer'})
<pymongo.results.InsertOneResult object at 0x000001D05B56FF08>
mydata.add_record({'id': 2, 'name':'Shyam Koirala', 'prof': 'Civil Engineer'})
<pymongo.results.InsertOneResult object at 0x000001D05B59C308>
mydata.count()
2
mydata.update_or_create({'id': 1, 'name':'Raju Gautam', 'prof': 'Software Engineer' })
<pymongo.results.UpdateResult object at 0x000002447A9AD448>
```