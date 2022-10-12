# Overview
In this guide we'll explore multiple ways to load data into an Astra database. The following examples and data are taken from the FREE [Introduction to Machine Learning Workshop](https://github.com/datastaxdevs/workshop-introduction-to-machine-learning/blob/cedrick-cli/README.md). If you want to go deeper, click the link to experience to full workshop up on GitHub.

**In this guide, we will**
- Create a database to explore data loading
- Use the Astra data loader to upload your own dataset
- Use DSBulk with the Astra Shell
- Verify both datasets using the CQL Console

# Prerequisites
While not required for ALL of the following sections you'll want to have 
- Access to a local terminal
- Java 8 or higher

## 1 Create a database to explore data loading
While you don't _have to_ use the following database and keyspace name, it would be best if you do to follow the examples below. If not, you'll have to replace out your own values.

First off, create a database with the following database and keyspace name with the button below. Once complete, come back here and continue in the next section.

**Database Name** = 
```shell 
workshops
```

**Keyspace Name** = 
```shell 
machine_learning
```

<<createDatabase>>

It should only take a couple minutes for your database to become `ACTIVE`. Once that occurs the guide will notify you and you can continue to the next step.

## 2 Use the Astra data loader to upload your own dataset
The Astra data loader is good for small sets of data (< 40MB) or data you want to experiment and test with. 

First thing, you'll need a **CSV** file to work with.

[DOWNLOAD movies.csv](https://raw.githubusercontent.com/riptano/astra-portal-getting-started/main/loadDataIntoAstraDB/movies.csv) <-- _right click on the `DOWNLOAD` link and choose **Save Link As**_

Now launch the data loader using the link below. This will open the loader in a separate tab. 

_You may want to view this side-by-side with this guide._

<<launchDataLoader>>

Once the loader is open follow the instructions for the `Upload your own dataset` section at the top. Use the socialMedia **CSV** file you just downloaded.

Here, you will see the field `Table Name`, a preview of the dataset, and the field `Partition keys`. Let's not worry about the details for now, just ensure each field has the following values.

**Table Name** _should already contain_
```shell
movies
```
_The loader will auto create this table for us_

**Partition Keys**
```shell
movieid
```

Move on to the next step and choose values for the `Target Database` and `Target Keypsace` fields.

**Target Database** _should already contain_
```shell
workshops
```
_This is the database we created earlier_

**Target Keypsace**
```shell
machine_learning
```
_This is the keyspace we created earlier to contain our tables._

Once all values are selected click **"Finish"**. 

At this point the dataset will be loaded in the background and you will receive both an email when the process starts and when the data is loaded. This shouldn't take too long, but for now, just move on to the **"Next"** step. We'll come back and verify the data later.

## 3 Use DSBulk with the Astra Shell
The [Astra Shell](https://awesome-astra.github.io/docs/pages/astra/astra-cli/) is a command line tool that includes commands for databases, streams, a CQL console, and data loading with DSBulk amongst other things.

#### 3a) Install Astra Shell
The first thing we'll need to do is install the Astra Shell. Execute the following commands in a local terminal.
```shell
curl -Ls "https://dtsx.io/get-astra-cli | bash"
```

#### 3b) Generate a token for access (you can use an exisitng token if you have one)
Now, let's setup the shell. We'll need to get an Astra token ready for this step. Tokens are used to securely authenticate and issue commands.

What's cool is one you pass the token to Astra Shell it will handle everything else for you. Use the following action to create a token if you don't already have one.

Recommended role = "Organization Administrator"

<<createToken>>

Great, now use the setup command, pass in your token when asked, and we'll load up some data.

```shell
astra setup
```

### 🖥️ Output

```yaml
+-------------------------------+
+-     Astra CLI SETUP         -+
+-------------------------------+

Welcome to Astra Cli. We will guide you to start.

[Astra Setup]
To use the cli you need to:
 • Create an Astra account on : https://astra.datastax.com
 • Create an Authentication token following: https://dtsx.io/create-astra-token

[Cli Setup]
You will be asked to enter your token, it will be saved locally in ~/. astrarc

• Enter your token (starting with AstraCS) : 
AstraCS:AAAAAA
[ INFO ] - Configuration Saved.


[cedrick.lunven@gmail.com]
ASTRA_DB_APPLICATION_TOKEN=AstraCS:AAAAAAAA

[What's NEXT ?]
You are all set.(configuration is stored in ~/.astrarc) You can now:
   • Use any command, 'astra help' will get you the list
   • Try with 'astra db list'
   • Enter interactive mode using 'astra'

Happy Coding !
```

Now, let's use the shell to get information about the `workshops` database we created earlier just to check everything is working as expected.
```shell
astra db get workshops
```

### 🖥️ Output

```yaml
+------------------------+------------------------------+
| Attribute              | Value                        |        
+------------------------+------------------------------+
| Name                   | workshops                    |        
| id                     | bb61cfd6-2702-4b19-97b6-3... |
| Status                 | ACTIVE                       |       
| Default Cloud Provider | AWS                          |       
| Default Region         | us-east-1                    |       
| Default Keyspace       | machine_learning             |       
| Creation Time          | 2022-08-29T06:13:06Z         |       
|                        |                              |       
| Keyspaces              | [0] machine_learning         |       
|                        |                              |        
|                        |                              |       
| Regions                | [0] us-east-1                |       
|                        |                              |       
+------------------------+------------------------------+
```

#### 3c) Start the CQL shell and connect to database `workshops` and keyspace `machine_learning`

```shell
astra db cqlsh workshops -k machine_learning
```

### 🖥️ Output

```yaml
[ INFO ] - Cqlsh has been installed

Cqlsh is starting please wait for connection establishment...
Connected to cndb at 127.0.0.1:9042.
[cqlsh 6.8.0 | Cassandra 4.0.0.6816 | CQL spec 3.4.5 | Native protocol v4]
Use HELP for help.
token@cqlsh:machine_learning> 
```

#### 3d) Initialize the Schema with `cqlsh`

```sql
CREATE TABLE IF NOT EXISTS socialmedia (
  status_id         INT,
  social_type       TEXT,
  num_reactions     INT,
  num_comments      INT,
  num_shares        INT,
  num_likes         INT,
  num_loves         INT,
  num_wows          INT,
  num_hahas         INT,
  num_sads          INT,
  num_angrys        INT,
  PRIMARY KEY (status_id)
);

quit;
```

#### 3e) Populate table `socialmedia`

```shell
astra db dsbulk workshops \
  load \
  -url https://raw.githubusercontent.com/riptano/astra-portal-getting-started/main/loadDataIntoAstraDB/socialMedia.csv \
  -c csv \
  -delim ',' \
  -m "status_id,social_type,num_reactions,num_comments,num_shares,num_likes,num_loves,num_wows,num_hahas,num_sads,num_angrys" \
  -header true \
  -k "machine_learning" \
  -t socialmedia
```

### 🖥️ Output
```yaml
DSBulk is starting please wait ...

total | failed | rows/s | p50ms |  p99ms | p999ms | batches
6,622 |      0 |  2,308 | 69.28 | 103.81 | 132.12 |    1.00
```

#### 3f) Check data load
If the previous command worked properly we should now see some data in the `socialmedia` table.
```shell
astra db cqlsh workshops -e "SELECT * FROM machine_learning.socialmedia LIMIT 5;"
```

## 4 Verify both datasets using the CQL Console
At this point, we've used both the **Astra Data Loader** and the **Astra Shell with DSBulk** to load the `movies` and `socialMedia` tables with data. 

In this final step we'll use the **CQL Console** to verify our data. Launch the **CQL Console below**.

<<launchCQLConsole>>

Now execute the following command in the console to verify both datasets.
```shell
SELECT * FROM machine_learning.movies LIMIT 5;
SELECT * FROM machine_learning.socialmedia LIMIT 5;
```

## 5 Summary 
In summary, we learned how to load data using both the **Astra Data Loader** and the **Astra Shell with DSBulk**. The **Astra Data Loader** is good for small sets of test or experimental data while the **Astra Shell with DSBulk** can handle larger sets of data that may need some time to load.

If you liked this guide and want to learn more, click the link in the **Recommended Guides** section below to learn about using `CRUD` operations to create, read, update, and delete data.

Happy coding and data loading 😃 

