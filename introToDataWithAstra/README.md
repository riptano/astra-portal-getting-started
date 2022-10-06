# Overview
Do cool shit be learning some CRUD operations in Astradatabase and infrastructure administration.

**In this guide, we will**
- Create an Astra DB instance
- Create tables
- Execute CRUD operations

## 1 Create your Astra DB instance
First off, create a database with the following database and keyspace name with the button below. Once complete, come back here and continue in the next section.

```shell
+---------------+------------------+
| Parameter     | Value            |
+---------------+------------------+
| Database Name | workshops        |
| Keyspace Name | chatsandra       |
+---------------+------------------+
```

<<createDatabase>>

## 2 Create tables
Ok, now that you have a database created the next step is to create tables to work with. 

### 2a Launch the CQL Console and login to the database
The command below will launch the Astra CQL Console in another tab. You may want to put the console and this guide side by side for easy copying.

<<launchCQLConsole>>


### 2b Describe keyspaces and USE the `chatsandra` one we just created
Ok, now we're ready to rock. Creating tables is quite easy, but before we create one we need to tell the database which keyspace we are working with.

First, let's **_DESCRIBE_** all of the keyspaces that are in the database. This will give us a list of the available keyspaces.

📘 **Command to execute**
```sql
DESC KEYSPACES;
```
_"desc" is short for "describe", either is valid._

> CQL commands usually end with a semicolon `;`. If you hit Enter, nothing happens and you don't even get your prompt back, most likely it's because you have not closed the command with `;`. If in trouble, you can always get back to the prompt with `Ctrl-C` and start typing the command anew.

Depending on your setup you might see a different set of keyspaces than in the image. The one we care about for now is **_chatsandra_**. From here, execute the **_USE_** command with the **_chatsandra_** keyspace to tell the database our context is within **_chatsandra_**.

> Take advantage of the TAB-completion in the CQL Console. Try typing `use cha` and then pressing TAB, for example.

📘 **Command to execute**
```sql
USE chatsandra;
```

Notice how the prompt displays ```<username>@cqlsh:chatsandra>``` informing us we are **using** the **_chatsandra_** keyspace. Now we are ready to create our table.

### 2c Create the `users` table
At this point we can execute a command to create the **users** table.
Just copy/paste the following command into your CQL console at the prompt.

📘 **Command to execute**

```sql
CREATE TABLE IF NOT EXISTS users ( 
  email       TEXT,
  name        TEXT,
  password    TEXT,
  user_id     UUID,
  PRIMARY KEY (( email ))
);
```

Then **_DESCRIBE_** your keyspace tables to ensure it is there.

📘 **Command to execute**

```sql
DESC TABLES;
```

Aaaand **BOOM**, you created a table in your database. That's it.
Now let's start working with data.

## 3 Execute CRUD operations
CRUD stands for "**create, read, update, and delete**". Simply put, they are the basic types of commands you need to work with ANY database in order to maintain data for your applications.

### 3a **(`C`)RUD** = create = insert data, users
We created the `users` table a moment ago, let's put some data in it. This is done with the **INSERT** statement. We'll start by inserting three rows into the **_users_** table.

Copy and paste the following in your CQL Console:
_(We provided a few variations to get a feel for the syntax needed.)_

📘 **Commands to execute**

```sql
INSERT INTO users (
  email,    // TEXT
  name,     // TEXT
  password, // TEXT
  user_id   // UUID: id of a user
)
VALUES (
  'otzi@mail.com',
  'Otzi Oney',
  '123456',
  11111111-1111-1111-1111-111111111111
);

INSERT INTO users (email, name, password, user_id) VALUES (
  'fred@qmail.net', 'Fred Fivey', 'qwerty',
  55555555-5555-5555-5555-555555555555
);
INSERT INTO users (email, name, password, user_id) VALUES (
  'nina@zmail.org', 'Nina Niney', 's3cr3t',
  99999999-9999-9999-9999-999999999999
);
```

### 3b **C(`R`)UD** = read = read data
Now that we've inserted a few rows, let's take a look at how to read the data back out. This is done with a **SELECT** statement.

```sql
// Read (some columns of) rows in a certain partition of "users" table
SELECT email, name, password FROM users
  WHERE user_id = 11111111-1111-1111-1111-111111111111;
```

### 3d **CR(`U`)D** = update = update data
At this point we've **_CREATED_** and **_READ_** some data, but what happens when you want to change some existing data to some new value? That's where **UPDATE** comes into play.

```sql
UPDATE users 
  SET email = 'otzi.oney@gmail.com' 
    WHERE user_id = 11111111-1111-1111-1111-111111111111
    AND   email = 'otzi@mail.com';

SELECT email, name, password FROM users
  WHERE user_id = 11111111-1111-1111-1111-111111111111;
```

That's it, we successfully edited a post (on both tables).
All that's left now is to **DELETE** some data.

### 3e **CRU(`D`)** = delete = remove data

The final operation from our **CRUD** acronym is **DELETE**. This is the operation we use when we want to remove data from the database.
In Apache Cassandra you can **DELETE** from the cell level all the way up to the partition
_(meaning I could remove a single column in a single row or I could remove a whole partition)_ using the same **DELETE** command.

_Generally speaking, it's best to perform as few delete operations as possible on the largest amount of data. Think of it this way, if you want to delete ALL data in a table, don't delete each individual cell, just **TRUNCATE** the table. If you need to delete all the rows in a partition, don't delete each row, **DELETE** the partition, and so on._

📘 **Commands to execute**

```sql
SELECT email, name, password FROM users;

DELETE FROM users
  WHERE user_id = 11111111-1111-1111-1111-111111111111;

SELECT email, name, password FROM users;
```

Notice now that we have one less user: it is as simple as that.
