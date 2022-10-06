# Overview
In this guide we'll explore multiple ways to load data into an Astra database. The following examples and data are taken from the FREE [Introduction to Machine Learning Workshop](https://github.com/datastaxdevs/workshop-introduction-to-machine-learning/blob/cedrick-cli/README.md). If you want to go deeper, click the link to experience to full workshop up on GitHub.

**In this guide, we will**
- Create a database to explore data loading
- Use the Astra data loader to load example data
- Use the Astra data loader to load YOUR data
- Use DSBulk with the Astra Shell

# Prerequisites
While not required for ALL of the following sections you'll want to have 
- Access to a local terminal
- Java 8 or higher

## 1 Create a database to explore data loading
While you don't _have to_ use the following database and keyspace name, it would be best if you do to follow the examples below. If not, you'll have to replace out your own values.

First off, create a database with the following database and keyspace name with the button below. Once complete, come back here and continue in the next section.

```
+---------------+------------------+
| Parameter     | Value            |
+---------------+------------------+
| Database Name | workshops        |
| Keyspace Name | machine_learning |
+---------------+------------------+
```

<<createDatabase>>

## 2 Use the Astra data loader to load example data

<<launchDataLoader>>


## 3 Use the Astra data loader to load YOUR data


## 4 Use DSBulk with the Astra Shell
The [Astra Shell](https://awesome-astra.github.io/docs/pages/astra/astra-cli/) is a command line tool that includes commands for databases, streams, a CQL console, and data loading with DSBulk amongst other things.

#### 4a) Install Astra Shell
The first thing we'll need to do is install the Astra Shell. Execute the following commands in a local terminal.
```shell
curl -Ls "https://dtsx.io/get-astra-cli"
```

#### 4b) Generate a token for access (you can use an exisitng token if you have one)
Now, let's setup the shell. We'll need to get an Astra token ready for this step. Tokens are used to securely authenticate and issue commands.

What's cool is one you pass the token to Astra Shell it will handle everything else for you. Use the following action to create a token if you don't already have one.

Recommended role = "Organization Administrator"

<<createToken>>

Great, now use the setup command, pass in your token when asked, and we'll load up some data.

```shell
astra setup
```

> 🖥️ Output
>
> ```
> +-------------------------------+
> +-     Astra CLI SETUP         -+
> +-------------------------------+
> 
> Welcome to Astra Cli. We will guide you to start.
> 
> [Astra Setup]
> To use the cli you need to:
 > • Create an Astra account on : https://astra.datastax.com
 > • Create an Authentication token following: https://dtsx.io/create-astra-token
> 
> [Cli Setup]
> You will be asked to enter your token, it will be saved locally in ~/. astrarc
> 
> • Enter your token (starting with AstraCS) : 
> AstraCS:AAAAAA
> [ INFO ] - Configuration Saved.
> 
> 
> [cedrick.lunven@gmail.com]
> ASTRA_DB_APPLICATION_TOKEN=AstraCS:AAAAAAAA
> 
> [What's NEXT ?]
> You are all set.(configuration is stored in ~/.astrarc) You can now:
>    • Use any command, 'astra help' will get you the list
>    • Try with 'astra db list'
>    • Enter interactive mode using 'astra'
> 
> Happy Coding !
> ```

Now, let's use the shell to get information about the `workshops` database we created earlier just to check everything is working as expected.
```shell
astra db get workshops
```

🖥️ Output

```
+------------------------+--------------------------------------+
| Attribute              | Value                                |
+------------------------+--------------------------------------+
| Name                   | workshops                            |
| id                     | bb61cfd6-2702-4b19-97b6-3b89a04c9be7 |
| Status                 | ACTIVE                               |
| Default Cloud Provider | AWS                                  |
| Default Region         | us-east-1                            |
| Default Keyspace       | machine_learning                     |
| Creation Time          | 2022-08-29T06:13:06Z                 |
|                        |                                      |
| Keyspaces              | [0] machine_learning                 |
|                        |                                      |
|                        |                                      |
| Regions                | [0] us-east-1                        |
|                        |                                      |
+------------------------+--------------------------------------+
```

#### 4c) Start the CQL shell and connect to database `workshops` and keyspace `machine_learning`

```shell
astra db cqlsh workshops -k machine_learning
```

> 🖥️ Output
>
> ```
> [ INFO ] - Cqlsh has been installed
> 
> Cqlsh is starting please wait for connection establishment...
> Connected to cndb at 127.0.0.1:9042.
> [cqlsh 6.8.0 | Cassandra 4.0.0.6816 | CQL spec 3.4.5 | Native protocol v4]
> Use HELP for help.
> token@cqlsh:machine_learning> 
> ```

#### 4d) Initialize the Schema with `cqlsh`

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

#### 4e) Populate table `socialmedia`

```shell
astra db dsbulk workshops \
  load \
  -url https://raw.githubusercontent.com/riptano/astra-portal-getting-started/main/loadDataIntoAstraDB/socialMedia.csv \
  -c csv \
  -delim ',' \
  -m "status_id,social_type,num_reactions,num_comments,num_shares,num_likes,num_loves,num_wows,num_hahas,num_sads,num_angrys" \
  -header false \
  -k "machine_learning" \
  -t socialmedia
```

> 🖥️ Output
>
> ```
> DSBulk is starting please wait ...
> 
> total | failed | rows/s | p50ms |  p99ms | p999ms | batches
> 6,622 |      0 |  2,308 | 69.28 | 103.81 | 132.12 |    1.00
> ```
