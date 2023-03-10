# Overview
Learn how to connect your app to Astra using Python.

**In this guide, you'll learn how to**
- Set up your Python development environment
- Connect to Astra DB and execute a static query
- Execute a query using a prepared statement

# Prerequisites
- You must have installed a recent version of Python 3.

## 1 Create a database
If you haven't already done so, create a new Astra DB database. 

_Creating a database only takes a couple of minutes. Feel free to move on while it's being created._

<<createDatabase>>

## 2 Build and verify your local Python development environment
You need both a local installation of Python 3 and the DataStax Python Driver for Apache Cassandra. To verify your Python installation, run the following command:

📘 **Command to execute**

```bash
python -V
```

You should see output similar to this:

```bash
Python 3.10.2
```

_If you do not, or if you get an error from that command, visit [https://www.python.org/downloads/](https://www.python.org/downloads/) for more information on downloads and installation instructions for your machine architecture._

To install The DataStax Python Driver for Apache Cassandra, you can use Pip (Python's package manager).

📘 **Command to execute**

```bash
pip install cassandra-driver
```

To verify your driver installation, run the following command:

📘 **Command to execute**

```bash
python -c 'import cassandra; print ("cassandra driver version = " + cassandra.__version__)'
```

You should see output similar to this:

```bash
cassandra driver version = 3.25.0
```

## 3 Set your Astra DB environment variables
In this section, have an Astra DB Token ready. If you need to create one, you can do that here: 

Recommended **role:** "Database Administrator"

<<createToken>>

For our new Python project, use two environment variables: **ASTRA_DB_TOKEN** and **ASTRA_DB_SECURE_BUNDLE_LOCATION**. Copy the token and run the below command to set it as an environment variable.

📘 **Command to execute**

```bash
export ASTRA_DB_TOKEN="AstraCS:qFDPGYOURASTRADBTOKENf15fc"
```

Create an environment variable containing the location of your (downloaded) secure bundle.  If you have not downloaded your secure bundle, you can do that here:

<<downloadSCB>>

Download it to your **~/Downloads** directory.  Feel free to copy it somewhere else if you like, but just make sure to refer to its location as shown here:

📘 **Command to execute**

```bash
export ASTRA_DB_SECURE_BUNDLE_LOCATION="/Users/yourusername/securebundledir/secure-connect-bundle.zip"
```

You can verify that these variables were set up correctly with the following command:

📘 **Command to execute**

```bash
env | grep ASTRA
```

## 4 Create a new project and connect to Astra DB
Start by creating a new Python program to connect to Astra DB.  Open your favorite IDE and create a new file called **testAstraDB.py**. Add the following three imports:

```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
```

This makes it possible for you to establish a secure connection (**PlainTextAuthProvider**) to your Astra DB cluster (**Cluster**).  You'll also need **os** to access the environment variables.

Next, create three variables in our Python code:

```python
username = "token"
token = os.environ['ASTRA_DB_TOKEN']
secureBundleLocation = os.environ['ASTRA_DB_SECURE_BUNDLE_LOCATION']
```

This defines the string "token" as our **username**, the **token** variable to our **ASTRA_DB_TOKEN** env var, and **secureBundleLocation** to our **ASTRA_DB_SECURE_BUNDLE_LOCATION** env var.

Define and configure our cluster:

```python
cloud_config= {
        'secure_connect_bundle': secureBundleLocation
}
auth_provider = PlainTextAuthProvider(username, token)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
```

Here, use your **secureBundleLocation** to set up your cloud configuration.  You're also initializing the **PlainTextAuthProvider**, and using both of these to configure our cluster object.

To finish, connect to your cluster and query the **local** table from the **system** keyspace to get the **cluster_name**.

```python
session = cluster.connect()

row = session.execute("select cluster_name from system.local").one()
if row:
    print("cluster name = " + row[0])
else:
    print("An error occurred.")
```

Running this code (with the two environment variables set appropriately) yields the following output:

```bash
cluster name = cndb
```

## 5 Using a prepared statement
Now that you know how to connect and run a static query, use a prepared statement. Prepared statements are good for queries that you plan on running several times for different key values.

Start by adding another import to your code. For this exercise, send in variables as arguments on the command line. To read those arguments, import the **sys** module.

```python
import sys
```

For this use case, read in a keyspace and table name, and then display the columns present in that table. Create variables in your code to read those arguments from the command line:

```python
keyspace = sys.argv[1]
table = sys.argv[2]
```

Next, create your query string and prepare it. Preparing your query string adds it to the prepared statement cache of your Astra DB cluster, preventing the need to parse it before each use.

```python
pStatement = session.prepare("""
    SELECT column_name FROM system_schema.columns WHERE keyspace_name=? AND table_name=?;
""")
```

Execute the prepared statement while passing the **keyspace** and **table** variables.  Then, process and display the results.

```python
rows = session.execute(pStatement,[keyspace,table])
print("\nColumns for " + keyspace + "." + table)
for row in rows:
    print(row[0])
```

When you run the code, be sure to pass the names of an existing **keyspace** and **table**:

📘 **Command to execute**

```bash
python testAstraDB.py system local
```

_For this example, use "**system**" (keyspace) and "**local**" (table name) to ensure you get some output. You can use whatever keyspace and table names you have access to in the database you are using._

<!-- The column names from the product table in the ecommerce keyspace (used in [DataStax's E-commerce Workshop](https://github.com/datastaxdevs/workshop-ecommerce-app#3-create-your-schema)) are shown.  Using another keyspace and table should produce results similar to this: -->

```bash
Columns for system.local
bootstrapped
broadcast_address
cluster_name
cql_version
data_center
dse_version
gossip_generation
graph
host_id
...
```

## 6 Summary
In summary, you learned to configure your local Python development environment. We've learned to use environment variables for referencing our Astra DB credentials and secure connect bundle. Finally, you've learned how to run a simple, static query – including how to query results with a prepared statement. This should provide a solid foundation for building more complex Python applications.

**Note**
The complete code for [testAstraDB.py](https://github.com/riptano/astra-portal-getting-started/blob/main/astraDBApplicationQuickstartPython/testAstraDB.py) can be found in this repo.

Here is the complete code block.
```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
import sys

username = "token"
token = os.environ['ASTRA_DB_TOKEN']
secureBundleLocation = os.environ['ASTRA_DB_SECURE_BUNDLE_LOCATION']

keyspace = sys.argv[1]
table = sys.argv[2]

cloud_config= {
        'secure_connect_bundle': secureBundleLocation
}
auth_provider = PlainTextAuthProvider(username, token)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select cluster_name from system.local").one()
if row:
    print("cluster name = " + row[0])
else:
    print("An error occurred.")

pStatement = session.prepare("""
    SELECT column_name FROM system_schema.columns WHERE keyspace_name=? AND table_name=?;
""")

rows = session.execute(pStatement,[keyspace,table])
print("\nColumns for " + keyspace + "." + table)
for row in rows:
    print(row[0])
```
