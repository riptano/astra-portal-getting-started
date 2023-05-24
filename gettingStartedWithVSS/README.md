# Overview
Discover how to set up a schema and load vector data with CQL, along with reading vector data using both CQL and Python. Get hands-on experience with actual code examples and the opportunity to try it out on your local machine. By the end of this guide, you’ll have a schema, data, and a working code example to play with.

**In this guide, we will**
- Learn about VSS
- Create a VSS enabled database
- Create a schema
- Load vector data with CQL
- Read vector data with CQL
- Read vector data with python
- Summarize what you learned

## 1 Learn about VSS
Vector Similarity Search (VSS) is a method of searching for similar vectors in a vector space. A vector is an array of numbers (floats) that represents a specific object or entity. In the context of databases, a vector could represent anything from an image to a document or even a user's behavior. VSS can be extremely useful in machine learning models, for instance in recommendation systems or image retrieval tasks where we want to find the most similar items to a given item.

## 2 Create a VSS enabled database
First, create a vector search enabled database with the following database and keyspace name with the button below.

**Database Name:** 
```shell 
vss_db
```

**Keyspace Name:** 
```shell 
vector_example
```

<<createDatabase>>
  
_This only takes a couple minutes. Once your database is ACTIVE, continue on to the next section._
  
## 3 Create a schema
The next step is to create tables.
  
### 3a Launch the CQL Console and login to the database
Open the CQL Console using the button below.
  
_You may want to put the console and this guide side by side for easy copying._
  
<<launchCQLConsole>>
  
### 3b Create a table with the VECTOR type
This table contains a VECTOR type example. Copy and paste the following command into your CQL console and press enter.
  
```sql
CREATE TABLE vector_example.products (
  id UUID PRIMARY KEY,
  name varchar,
  description varchar,
  item_vector VECTOR<float, 3>
);
```
```sql
CREATE CUSTOM INDEX item_ann_index ON vector_example.products(item_vector) USING 'VectorMemtableIndex'; ?????
```
```sql
CREATE CUSTOM INDEX ann_index on vector_example.foo(j) using 'StorageAttachedIndex' ?????
```

## 4 Load vector data with CQL
We created the products table in the step above with a VECTOR type. Now we’ll insert some data into the table using the new type.

```sql
insert into vector_example.foo (i, j) values (1, [8, 2.3, 58])
insert into vector_example.foo (i, j) values (2, [1.2, 3.4, 5.6])
insert into vector_example.foo (i, j) values (5, [23, 18, 3.9])
```

## 5 Read vector data with CQL
Now take a look at how to read the data with a SELECT statement.

```sql
SELECT * FROM vector_example.products WHERE item_vector ANN OF [3.4, 7.8, 9.1];
```

## 6 Read vector data with python
Now that you’ve executed some basic CQL commands using VECTOR, take this to the next step and experiment with some python code. 
You’ll need to do this next part on your local machine. Ensure you have at least python version 3.10 installed and ready to go.
  
### 6a Install python dependencies
First thing, install the cassandra driver and the os library.

```python
pip install cassandra-driver
```
```python
pip install os
```
  
### 6b Copy and configure example python code
In order to connect the example application to your vector search enabled database, you’ll need a couple items first.

In this section, have an Astra DB Token ready. If you need to create one, you can do that here. Be sure to keep this information handy. 

_You will need both the CLIENT_ID and CLIENT_SECRET values from the generated token._

Recommended role: "Database Administrator"

<<createToken>>

Now, download the secure connect bundle for this database.

<<secureBundle>>

Copy the following code into a file called ‘vector_example.py’ and paste in the SECURE_CONNECT_BUNDLE_PATH, ASTRA_CLIENT_ID, and ASTRA_CLIENT_SECRET variables from the information provided a moment ago.

```python
import os

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<PATH_TO_YOUR SECURE_BUNDLE>>')
ASTRA_CLIENT_ID = '<<YOUR_CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<YOUR_CLIENT_SECRET>>'
KEYSPACE_NAME = 'vector_example'

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
   'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.execute("create table {KEYSPACE_NAME}.foo(i int primary key, j float vector[3])")
session.execute("create custom index ann_index on {KEYSPACE_NAME}.foo(j) using 'StorageAttachedIndex'")
session.execute("insert into {KEYSPACE_NAME}.foo (i, j) values (1, [8, 2.3, 58])")
session.execute("insert into {KEYSPACE_NAME}.foo (i, j) values (2, [1.2, 3.4, 5.6])")
session.execute("insert into {KEYSPACE_NAME}.foo (i, j) values (5, [23, 18, 3.9])")
for row in session.execute("select j from {KEYSPACE_NAME}.foo where j ann of [3.4, 7.8, 9.1] limit 1"):
   results = row[0]
   assert len(results) == 3
   print(results)

# Close the connection
cluster.shutdown()
```
  
### 6c Execute example python code

```bash
python vector_example.py
```
  
# 7 Summarize what you learned
Wrapping up, this guide has empowered you with Vector Similarity Search (VSS) basics. You've built a VSS-enabled Astra database, interacted with vector data using CQL and Python, and applied hands-on code examples. This is just a taste of what is to come.

