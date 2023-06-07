# Overview
Discover how to set up a schema and load vector data with CQL, along with reading that vector data using both CQL and Python. Get hands-on experience with actual code examples and the opportunity to try it out on your local machine. By the end of this guide, you’ll have a schema, data, and a working code example to play with.

## 1 Learn about Vector Search
Vector Search is a method of searching for similar vectors in a vector space. A vector is an array of numbers (floats) that represents a specific object or entity. In the context of databases, a vector could represent anything from an image to a document or even a user's behavior. Vector Search can be extremely useful in machine learning models, for instance in recommendation systems or image retrieval tasks where we want to find the most similar items to a given item.

Now that you have a better understanding of what a vector is and how it’s used, let’s create a vector-enabled database and explore a bit.

## 2 Create a database with Vector Search
First, create a vector-enabled database with the following database and keyspace name with the button below.

**Database Name:** 
```shell 
vector_search_db
```

**Keyspace Name:** 
```shell 
vsearch
```

<<createVectorDatabase>>
  
_This only takes a couple minutes. Once your database is ready, continue on to the next section._
  
## 3 Create a table
Start by opening the CQL console with the button below. This will open the CQL console in a new tab, which should allow for easier copying of the following code blocks.
  
<<launchCQLConsole>>
  
### Create a table with the VECTOR type
This table contains a VECTOR type example. Copy and paste the following commands into your CQL console and press enter.
  
```sql
CREATE TABLE IF NOT EXISTS vsearch.products (
  id int PRIMARY KEY,
  name TEXT,
  description TEXT,
  item_vector VECTOR<FLOAT, 5> //create a 5-dimensional embedding
);

CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON vsearch.products(item_vector) USING 'StorageAttachedIndex';
```

_Embedding vectors usually have several hundred dimensions: here, for the sake of clarity, we will work with a simplified embedding space with just five dimensions._

## 4 Load vector data with CQL
You created the **products** table in the step above with a VECTOR type. Now insert the following data into the table using the new type.

```sql
INSERT INTO vsearch.products (id, name, description, item_vector) 
VALUES (
   1, //id
   'Coded Cleats', //name
   'ChatGPT integrated sneakers that talk to you', //description
   [0.1, 0.15, 0.3, 0.12, 0.05] //item_vector
);

INSERT INTO vsearch.products (id, name, description, item_vector) 
   VALUES (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [0.45, 0.09, 0.01, 0.2, 0.11]);

INSERT INTO vsearch.products (id, name, description, item_vector) 
   VALUES (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [0.1, 0.05, 0.08, 0.3, 0.6]);
```

_In the context of Vector Search, a vector is an array of numbers (floats) that represents a specific object or entity. The numbers in the vector are features that describe the object or entity._

_Note that the vectors above are a fictional, albeit somewhat realistic example. Usually embedding vectors have unit length, but this does not have to always be the case. In fact, you can do any kind of vector search with Astra DB, not limited to embeddings: for instance, you could use this feature to locate the star system closest to a given point in the universe, provided you have its 3-D coordinates…_

## 5 Read vector data with CQL
Let's say a customer entered "An AI-powered display to alter how I feel" in the search box of the e-commerce website. The superpower of embedding vectors is that they can turn such a description into a vector as well, say [0.15, 0.1, 0.1, 0.35, 0.55], that happens to be geometrically closer to the item with the most similar description.
So, once you get the embedding function to output this vector for the search-box sentence, all you have to do is to search the table for a similar item.

Let's look for a similar item with a SELECT statement.

```sql
SELECT * FROM vsearch.products ORDER BY item_vector ANN OF [0.15, 0.1, 0.1, 0.35, 0.55] LIMIT 1;
```

## 6 Read vector data with Python
Now that you’ve executed some basic CQL commands using the new vector data type, take this to the next level and experiment with some Python code.

You’ll need to do this next part on your _localhost_. Ensure you have at least Python 3.8 installed and ready to go.
  
### Install Python dependencies
First, install the Cassandra Python driver with the following command on your _localhost_.

```python
pip install cassandra-driver
```
_Depending on your OS and installed Python versions, you might need to use “pip3” for the command above._
  
### Copy and configure example Python code
In order to connect the example application to your vector-search enabled database, you’ll need a couple items first:

Have an Astra DB Token ready. If you need to create one, you can do that here. Be sure to keep this information handy. 
   - **Recommended Role:** Database Administrator
   - You will need both the **CLIENT_ID** and **CLIENT_SECRET** values from the generated token

<<createToken>>

Now, download the Secure Connect Bundle for this database.

<<downloadSCB>>

Copy the following code into a file named ‘vector_example.py’ and update the values for the following variables: 
- **SECURE_CONNECT_BUNDLE_PATH**
- **ASTRA_CLIENT_ID**
- **ASTRA_CLIENT_SECRET** 

```python
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<YOUR_SECURE_CONNECT_BUNDLE_PATH>>')
ASTRA_CLIENT_ID = '<<YOUR_CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<YOUR_CLIENT_SECRET>>'

KEYSPACE_NAME = 'vsearch'
TABLE_NAME = 'products'

print("Starting guide example")

cloud_config = {
   'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

print(f"Creating table {TABLE_NAME} in keyspace {KEYSPACE_NAME}")
session.execute(f"CREATE TABLE IF NOT EXISTS {KEYSPACE_NAME}.{TABLE_NAME} (id int PRIMARY KEY, name TEXT, description TEXT, item_vector VECTOR<FLOAT, 5>)")

print(f"Creating index ann_index on table {TABLE_NAME} and inserting example data")
session.execute(f"CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON {KEYSPACE_NAME}.{TABLE_NAME}(item_vector) USING 'StorageAttachedIndex'")

product_data = [
    (1, 'Coded Cleats', 'ChatGPT integrated sneakers that talk to you', [0.1, 0.15, 0.3, 0.12, 0.05]),
    (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [0.45, 0.09, 0.01, 0.2, 0.11]),
    (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [0.1, 0.05, 0.08, 0.3, 0.6])
]

for product in product_data:
    session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES {product}")

print(f"Returning 'nearest neighbor' using ANN search")
for row in session.execute(f"SELECT name, description, item_vector FROM {KEYSPACE_NAME}.{TABLE_NAME} ORDER BY item_vector ANN OF [0.15, 0.1, 0.1, 0.35, 0.55] LIMIT 1"):
   print("\t" + str(row))

cluster.shutdown()
```

### Run your code!
```python
python vector_example.py
```
_Depending on your OS and installed Python versions, you might need to use “python3” for the command above._
  
## 7 Summarize what you learned
Wrapping up, this guide has empowered you with Vector Search basics. You've built a vector-enabled database, interacted with vector data using CQL and Python, and applied hands-on code examples. This is just a taste of what is to come.

Now that you’re done learning about the vector data type in Astra DB, you should explore [CassIO](https://cassio.org). Its purpose is to simplify database access for Generative AI or other Machine Learning workloads, providing ready-to-use tools for easy integration of Astra DB and Apache Cassandra in your next AI application.

Here’s a code excerpt from [CassIO](https://cassio.org). Click the “[Getting Started with CassIO](https://cassio.org)” link to learn more.

```python
from langchain.vectorstores.cassandra import Cassandra

index_creator = VectorstoreIndexCreator(
vectorstore_cls=Cassandra,
embedding=myEmbedding,
...
)

loader = TextLoader('texts/amontillado.txt', encoding='utf8')
index = index_creator.from_loaders([loader])

answer = index.query("Who is Luchesi?")
```

Happy searching 🎉