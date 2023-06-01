# Overview
Discover how to set up a schema and load vector data with CQL, along with reading that vector data using both CQL and Python. Get hands-on experience with actual code examples and the opportunity to try it out on your local machine. By the end of this guide, you’ll have a schema, data, and a working code example to play with.

**In this guide, you will**
- Learn about vector Search
- Create a Vector Search enabled database
- Create a schema
- Load vector data with CQL
- Read vector data with CQL
- Read vector data with python
- Summarize what you learned

## 1 Learn about Vector Seach
Vector Search is a method of searching for similar vectors in a vector space. A vector is an array of numbers (floats) that represents a specific object or entity. In the context of databases, a vector could represent anything from an image to a document or even a user's behavior. Vector Search can be extremely useful in machine learning models, for instance in recommendation systems or image retrieval tasks where we want to find the most similar items to a given item.

## 2 Create a Vector Search enabled database
First, create a vector search enabled database with the following database and keyspace name with the button below.

**Database Name:** 
```shell 
vector_search_db
```

**Keyspace Name:** 
```shell 
vsearch
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
CREATE TABLE IF NOT EXISTS vsearch.products (
  id int PRIMARY KEY,
  name varchar,
  description varchar,
  item_vector VECTOR<float, 3> //create a vector with 3 values
);
```

```sql
CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON vsearch.products(item_vector) USING 'StorageAttachedIndex';
```

## 4 Load vector data with CQL
You created the _products_ table in the step above with a VECTOR type. Now insert the following data into the table using the new type.

```sql
INSERT INTO vsearch.products (id, name, description, item_vector) 
VALUES (
   1, //id
   'Coded Cleats', //name
   'ChatGPT integrated sneakers that talk to you', //description
   [8, 2.3, 58] //price, weight, numReviews
);
INSERT INTO vsearch.products (id, name, description, item_vector) 
   VALUES (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [1.2, 3.4, 5.6]);
INSERT INTO vsearch.products (id, name, description, item_vector) 
   VALUES (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [23, 18, 3.9]);
```

In the context of Vector Search, a vector is an array of numbers (floats) that represents a specific object or entity. The numbers in the vector are features that describe the object or entity.

In the examples given, _item_vector_ is a VECTOR type. Each array that you're inserting into _item_vector_ ([8, 2.3, 58], [1.2, 3.4, 5.6], [23, 18, 3.9]) is a vector. These vectors might represent anything from an image to a document or even a user's behavior. The specific meaning of the numbers in each vector depends on the context in which they're used.

For instance, if you were using vectors to represent products in an ecommerce application, the numbers in the vector could represent various characteristics of each product - things like its price, weight, or number of reviews. If the vectors represented user behavior, they might include things like the number of times a user visited a certain page, the number of items they purchased, etc.

These numbers are a compact way to represent complex data in a way that makes it easy to compare and contrast different entities (like products or user behaviors) in a vector space. That's what makes Vector Similarity Search a powerful tool for tasks like recommendation systems, image retrieval, and many others.

## 5 Read vector data with CQL
Now take a look at how to read the data with a SELECT statement.

```sql
SELECT * FROM vsearch.products WHERE item_vector ANN OF [3.4, 7.8, 9.1] LIMIT 1;
```

Given the explanation above, this query is asking "give me the item most similar in price (3.4), weight (7.8), and number of reviews (9.1)" compared to the other products in the table.

_The vector values themselves are arbitrary and based on the dataset and embeddings used. They could be just about any range of floats._

## 6 Read vector data with python
Now that you’ve executed some basic CQL commands using the new vector data type, take this to the next level and experiment with some python code.

You’ll need to do this next part on your _localhost_. Ensure you have at least Python 3.8 installed and ready to go.
  
### 6a Install python dependencies
First, install the Cassandra Python driver with the following command on your _localhost_.

```python
pip install git+https://github.com/datastax/python-driver.git@cep-vsearch#egg=cassandra-driver
```
```python
pip install os
```
  
### 6b Copy and configure example python code
In order to connect the example application to your vector search enabled database, you’ll need a couple items first:

- Have an Astra DB Token ready. If you need to create one, you can do that here. Be sure to keep this information handy. 
   - You will need both the CLIENT_ID and CLIENT_SECRET values from the generated token.
   - Recommended role: "Database Administrator"

<<createToken>>

- Now, download the secure connect bundle for this database.

<<downloadSCB>>

Copy the following code into a file called ‘vector_example.py’ and paste in the SECURE_CONNECT_BUNDLE_PATH, ASTRA_CLIENT_ID, and ASTRA_CLIENT_SECRET **variables from the information provided a moment ago**.

```python
import os

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<PATH_TO_YOUR SECURE_BUNDLE>>')
ASTRA_CLIENT_ID = '<<YOUR_CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<YOUR_CLIENT_SECRET>>'
KEYSPACE_NAME = 'vsearch'

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
  
## 7 Summarize what you learned
Wrapping up, this guide has empowered you with Vector Search basics. You've built a VSS-enabled Astra database, interacted with vector data using CQL and Python, and applied hands-on code examples. This is just a taste of what is to come.

Happy searching.