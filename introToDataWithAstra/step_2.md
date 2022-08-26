# Create tables
Ok, now that you have a database created the next step is to create tables to work with. 

> _General Methodology Note_: We'll work with a (rather simplified) "chat application" called **ChatSandra**:
> users, identified by a unique ID, write posts in several "rooms".
> Rooms are also uniquely identified by their name, such as `#gardening`. The design of our application is such
> that we need to be able to (a) retrieve all posts by a given user, sorted by descending date,
> and (b) retrieve all posts for a given room, sorted by descending date.
> As dictated by the best practices of data modeling with Cassandra, these requirements are satisfied by creating _two_ very similar tables (denormalization),
> as you'll see momentarily: they will contain the same posts, but stored (a.k.a. partitioned) in two different ways;
> and it will be our (that is, the application's) responsibility to maintain them aligned.
> Of course, we also need a `users` table - we will start with this one indeed.

**✅ Step 2a. Navigate to the CQL Console and login to the database**

<<LaunchCQLConsole>> 


**✅ Step 2b. Describe keyspaces and USE one of them**

Ok, now we're ready to rock. Creating tables is quite easy, but before we create one we need to tell the database which keyspace we are working with.

First, let's **_DESCRIBE_** all of the keyspaces that are in the database. This will give us a list of the available keyspaces.

📘 **Command to execute**
```sql
DESC KEYSPACES;
```
_"desc" is short for "describe", either is valid._

> CQL commands usually end with a semicolon `;`. If you hit Enter, nothing happens and you don't even get your prompt back, most likely it's because you have not closed the command with `;`. If in trouble, you can always get back to the prompt with `Ctrl-C` and start typing the command anew.

📗 **Expected output**

![Keyspaces in CQL](images/cql/01_desc_keyspaces.png)

Depending on your setup you might see a different set of keyspaces than in the image. The one we care about for now is **_chatsandra_**. From here, execute the **_USE_** command with the **_chatsandra_** keyspace to tell the database our context is within **_chatsandra_**.

> Take advantage of the TAB-completion in the CQL Console. Try typing `use cha` and then pressing TAB, for example.

📘 **Command to execute**
```sql
USE chatsandra;
```

📗 **Expected output**

![USE keyspace](images/cql/02_use_chatsandra.png)

Notice how the prompt displays ```<username>@cqlsh:chatsandra>``` informing us we are **using** the **_chatsandra_** keyspace. Now we are ready to create our table.

**✅ Step 2c. Create the users table**

At this point we can execute a command to create the **users** table.
Just copy/paste the following command into your CQL console at the prompt.
Try to identify the primary key, the partition key and the clustering columns
(if any) for this table in the command:

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
📗 **Expected output**

![A table created](images/cql/03_user_table_created.png)

Aaaand **BOOM**, you created a table in your database. That's it.
Now let's go ahead and create a couple more tables before we do
something interesting with the data.

**✅ Step 2d. Create the tables for posts**

Let us create two more tables, which will contain the _posts_.
As remarked earlier, we will store the posts in two tables which
differ in how they are partitioned: look at the commands below,
the differences mostly lie in the `PRIMARY KEY` specification:

📘 **Command to execute**

```sql
CREATE TABLE IF NOT EXISTS posts_by_user ( 
  user_id     UUID, 
  post_id     TIMEUUID,
  room_id     TEXT, 
  text        TEXT,
  PRIMARY KEY ((user_id), post_id)
) WITH CLUSTERING ORDER BY (post_id DESC);

CREATE TABLE IF NOT EXISTS posts_by_room ( 
  room_id     TEXT, 
  post_id     TIMEUUID,
  user_id     UUID,
  text        TEXT,
  PRIMARY KEY ((room_id), post_id)
) WITH CLUSTERING ORDER BY (post_id DESC);
```

Then **_DESCRIBE_** your keyspace tables: you should see all three listed.

📘 **Command to execute**

```sql
DESC TABLES;
```

📗 **Expected output**

![A table created](images/cql/04_post_tables_created.png)

_You may wonder, how did we arrive at this particular structure for the post tables?
The answer lies in the methodology for data modeling
with Cassandra, which, at its very core, states: **first look at the application's needs,
determine the required workflows, then map them to a number of queries, finally design a table around each query**.
We create table **_posts_by_user_** to support a query such as "get all posts by a user X";
then we also need table **_posts_by_room_** for a query of type "get all posts in room Y".
The two tables have the same columns, but the different choice of partition key is what
will make the two queries possible on the respective tables._