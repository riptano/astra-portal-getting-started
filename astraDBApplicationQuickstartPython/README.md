# Overview
In this guide we'll explore connecting your app to Astra using Python.

**In this guide, we will learn how to**
- Set up our Python development environment
- Connect to Astra DB and execute a static query
- Execute a query using a prepared statement

# Prerequisites
- You should have an Astra account.
- You should [Create an Astra Database](../overviewOfAstraDB#4-how-to-create-an-astra-database-with-the-ui-).
- You should Have an Astra Token and have downloaded your Secure bundle.
- You should have a recent version of Python 3.

# Guide
## 1. Build and verify your local Python development environment.

For this guide, you will need both a local installation of Python 3 and the DataStax Python Driver for Apache Cassandra.  To verify your Python installation, run the following command:

```bash
python -V
```

You should see output similar to this:

```bash
Python 3.10.2
```

If you do not, or if you get an error from that command, visit https://www.python.org/downloads/ for more information on downloads and installation instructions for your machine architecture.

To install The DataStax Python Driver for Apache Cassandra, you can use Pip (Python's package manager).

```bash
pip install cassandra-driver
```

To verify your driver installation, run the following command:

```bash
python -c 'import cassandra; print ("cassandra driver version = " + cassandra.__version__)'
```

You should see output similar to this:

```bash
cassandra driver version = 3.25.0
```

## 2. Set your Astra DB environment variables

For our new Python project, we're going to use two environment variables: `ASTRA_DB_TOKEN` and `ASTRA_DB_SECURE_BUNDLE_LOCATION`.  Copy the token from the CSV file you downloaded from astra.datastax.com.  Run the below command to set it as an environment variable.

```bash
export ASTRA_DB_TOKEN="AstraCS:qFDPGYOURASTRADBTOKENf15fc"
```

You will also need to create an environment variable containing the location of your (downloaded) secure bundle.

```bash
export ASTRA_DB_SECURE_BUNDLE_LOCATION="/Users/yourusername/securebundledir/secure-connect-bundle.zip"
```

You can verify that these variables were set up correctly with the following command:

```bash
env | grep ASTRA
```

## 3. Create a new project and connect to Astra DB

Let's start by creating a new Python program to connect to Astra DB.  Open your favorite IDE and create a new file called `testAstraDB.py`.  We will start by adding three imports:

```python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
```

This makes it possible for you to establish a secure connection (`PlainTextAuthProvider`) to your Astra DB cluster (`Cluster`).  We'll also need `os` to access the environment variables.

Next, we'll create three variables in our Python code:

```python
username = "token"
token = os.environ['ASTRA_DB_TOKEN']
secureBundleLocation = os.environ['ASTRA_DB_SECURE_BUNDLE_LOCATION']
```

This defines the string "token" as our `username`, the `token` variable to our `ASTRA_DB_TOKEN` env var, and `secureBundleLocation` to our `ASTRA_DB_SECURE_BUNDLE_LOCATION` env var.  Next, we'll define and configure our cluster:

```python
cloud_config= {
        'secure_connect_bundle': secureBundleLocation
}
auth_provider = PlainTextAuthProvider(username, token)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
```

Here, we're using our `secureBundleLocation` to set up our cloud configuration.  We're also initializing the `PlainTextAuthProvider`, and using both of these to configure our cluster object.

To finish up, we'll connect to our cluster and query the `local` table from the `system` keyspace to get the `cluster_name`.

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

## 4. Using a prepared statement

Now that we've shown how to connect and run a static query, let's use a prepared statement.  Prepared statements are good for queries that we plan on running several times for different key values.

Let's start by adding another import to our code.  For this exercise, we'll send in variables as arguments on the command line.  To read those arguments, we'll need to import the `sys` module.

```python
import sys
```

Or, you can edit the exiting `import` for the `os` module, adding `sys` like this:

```python
import os, sys
```

For our use case, we'll read in a keyspace and table name, and then display the columns present in that table.  Let's create variables in our code to read those arguments from the command line:

```python
keyspace = sys.argv[1]
table = sys.argv[2]
```

Next, we'll create our query string and prepare it.  Preparing our query adds it to the prepared statement cache of our Astra DB cluster, preventing it from needing to be parsed before each use.

```python
pStatement = session.prepare("""
    SELECT column_name FROM system_schema.columns WHERE keyspace_name=? AND table_name=?;
""")
```

Now, we'll execute the prepared statement while passing the `keyspace` and `table` variables.  Then, we will process and display the results.

```python
rows = session.execute(pStatement,[keyspace,table])
print("\nColumns for " + keyspace + "." + table)
for row in rows:
    print(row[0])
```

When you run the code, be sure to pass the names of an existing keyspace and table:

```bash
python testAstraDB.py ecommerce product
```

For this example, the column names from the product table in the ecommerce keyspace (used in [DataStax's E-commerce Workshop](https://github.com/datastaxdevs/workshop-ecommerce-app#3-create-your-schema)) are shown.  Using another keyspace and table should produce results similar to this:

```bash
Columns for ecommerce.product
brand
images
linked_documents
long_desc
model_number
name
product_group
product_id
short_desc
specifications
```

## 5. Summary

In summary, we have talked through configuring our local Python development environment, and using environment variables to reference our Astra DB credentials and secure connect bundle.  We have also show how to run a simple, static query, as well as how to query results using a prepared statement.  This should provide a solid foundation for building more complex Python applications.

Note, that the complete code for [testAstraDB.py](./testAstraDB.py) can be found in this repo.
