## 3. Execute CRUD operations
CRUD stands for "**create, read, update, and delete**". Simply put, they are the basic types of commands you need to work with ANY database in order to maintain data for your applications.

**✅ Step 3a. (C)RUD = create = insert data, users**

Our tables are in place so let's put some data in them. This is done with the **INSERT** statement. We'll start by inserting three rows into the **_users_** table.

> _Note_ that we have three users in this example: "111...", "555..." and "999...", which are having some pleasant conversations. In a real application, you would probably
> generate user IDs at the application level or with the `UUID()` primitive offered by CQL.
> See the [documentation](https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/timeuuid_functions_r.html) for more details on time/uuid-related CQL functions.

Copy and paste the following in your CQL Console:
_(Once you have carefully examined the first of the following **INSERT** statements below, you can simply copy/paste the others which are very similar.)_

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

**✅ Step 3b. (C)RUD = create = insert data, posts**

Let's run some more **INSERT** statements, this time for **posts**. We'll insert data into the **_posts_by_user_** table.
_(Once you have carefully examined the first of the following **INSERT** statements below, you can simply copy/paste the others which are very similar.)_

> _Note_: in the following, we are using `TIMEUUID`s crafted by hand, to make things easier to visualize. In a real application, you would generate them at application
> level or, in some cases, using the `NOW()` primitive offered by CQL. In the values below, you can just pay attention to the first octet of hex digits.

📘 **Commands to execute**

```sql
// Insert some data in the "posts_by_user" table

INSERT INTO posts_by_user (
  user_id,  // UUID: unique id for a user
  post_id,  // TIMEUUID: unique uuid + timestamp
  room_id,  // TEXT: id of a chat room
  text      // TEXT: the post content itself
)
VALUES (
  11111111-1111-1111-1111-111111111111,
  22222222-5cff-11ec-be16-1fedb0dfd057,
  '#hiking',
  'I climbed Mt. Gumbo yesterday ...'
);

INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  77777777-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'Who likes marathons here?'
);
INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  aaaaaaaa-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', '... and Mt. Gumbo was easy!!!'
);
INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  55555555-5555-5555-5555-555555555555,
  bbbbbbbb-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', 'For us humans Gumbo is a tough one...!'
);
INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  99999999-9999-9999-9999-999999999999,
  cccccccc-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'I just love marathons.'
);
INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  eeeeeeee-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'Same here!'
);
INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
  55555555-5555-5555-5555-555555555555,
  ffffffff-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', 'I have to buy new boots.'
);
```

Ok, we have a lovely bunch of posts in our chat application.
But **wait**: data is denormalized and the very same posts have to be inserted
in table **_posts_by_room_** as well! Let's do it with the following command
(please note that the `INSERT` statements are exactly the same as above,
with only the table name changed):

📘 **Commands to execute**

```sql
// Insert some data in the "posts_by_room" table

INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  22222222-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', 'I climbed Mt. Gumbo yesterday ...'
);

INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  77777777-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'Who likes marathons here?'
);
INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  aaaaaaaa-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', '... and Mt. Gumbo was easy!!!'
);
INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  55555555-5555-5555-5555-555555555555,
  bbbbbbbb-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', 'For us humans Gumbo is a tough one...!'
);
INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  99999999-9999-9999-9999-999999999999,
  cccccccc-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'I just love marathons.'
);
INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  11111111-1111-1111-1111-111111111111,
  eeeeeeee-5cff-11ec-be16-1fedb0dfd057,
  '#running', 'Same here!'
);
INSERT INTO posts_by_room (user_id, post_id, room_id, text) VALUES (
  55555555-5555-5555-5555-555555555555,
  ffffffff-5cff-11ec-be16-1fedb0dfd057,
  '#hiking', 'I have to buy new boots.'
);
```

**✅ Step 3c. C(R)UD = read = read data**

Now that we've inserted a set of rows (two sets, to be precise), let's take a look at how to read the data back out. This is done with a **SELECT** statement. In its simplest form we could just execute a statement like the following **_**cough_** **_**cough_**:
```sql
// Read all rows from "posts_by_user" table (careful with this ...)
SELECT * FROM posts_by_user;
```

You may have noticed my coughing fit a moment ago. Even though you can execute a **SELECT** statement with no partition key defined, this is NOT something you should do when using Apache Cassandra. We are doing it here for illustration purposes only and because our whole dataset is just a handful of values.
Given the data we inserted earlier, a more proper statement would be something like (while we are at it, we also explicitly specify which columns we want back):
```sql
// Read (some columns of) rows in a certain partition of "posts_by_user" table
SELECT post_id, room_id, text FROM posts_by_user
  WHERE user_id = 11111111-1111-1111-1111-111111111111;
```

The key is to ensure we are **always selecting by some partition key** at a minimum, so to avoid the dreaded _full-cluster scans_ which yield performances that are generally unacceptable in production.

Ok, with that out of the way we can **READ** the data from the other table as well - remember we **INSERT**ed on both tables?

📘 **Commands to execute**

```sql
// Read the whole "posts_by_room" table
// (warning: not suitable for large tables in production)
SELECT * FROM posts_by_room;

// Read (some columns of) posts from a certain room (= a certain partition)
SELECT user_id, text FROM posts_by_room WHERE room_id = '#hiking';
```

(again, in the second **SELECT** we specify some columns - it is something we may want to do in most cases).

📗 **Expected output**

![SELECT in CQL](images/cql/05_selects.png)

_Notice how the two tables contain the same set of posts, but group them differently:
table `posts_by_user` is partitioned by user, while table `posts_by_room` is partitioned by room - and the corresponding outputs
reflect this fact.
This is very much related to the fact that these two tables, in the data modeling process, were designed
to answer two different questions, "what are the posts by user X?" and "what are the posts in room Y?" respectively.
Moreover, within any partition in both tables, right as we required when creating the table,
posts are kept (and displayed) sorted by decreasing `post_id` (which, due to the nature of `TIMEUUID`s,
implies a time-ordering as well)._

Once you execute the above **SELECT** statements you should see something like the expected output above. We have now **READ** the data we **INSERTED** earlier. Awesome job!

_BTW, just a little extra for those who are interested. Since we used a [TIMEUUID](https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/timeuuid_functions_r.html) type for our **post_id** field we can use the **dateOf()** function to determine the timestamp from the value. Check it out._

```sql
// Read all data from the posts_by_room table, 
// convert post_id into a timestamp, and label the column "post_date"
SELECT user_id, dateOf(post_id) AS post_date, text FROM posts_by_room
  WHERE room_id = '#hiking';
```

**✅ Step 3d. CR(U)D = update = update data**

At this point we've **_CREATED_** and **_READ_** some data, but what happens when you want to change some existing data to some new value? That's where **UPDATE** comes into play.
_The use case is as follows: in our chat app, users are allowed to edit their previous posts._

Let's take one of the records we created earlier and modify it. Recall that we **_INSERTED_** the following record in the **_posts_by_user_** table.
```sql
      // ** Just for reference: **
      //  INSERT INTO posts_by_user (user_id, post_id, room_id, text) VALUES (
      //    11111111-1111-1111-1111-111111111111,
      //    aaaaaaaa-5cff-11ec-be16-1fedb0dfd057,
      //    '#hiking', '... and Mt. Gumbo was easy!!!'
      //  );
```

Let's also take a look at how the **_posts_by_user_** table was created. In order to **UPDATE** an existing record, indeed, we need to know the primary key we defined when we **CREATE**d the table.
```sql
      // ** Just for reference: **
      // CREATE TABLE IF NOT EXISTS posts_by_user ( 
      //   user_id     UUID, 
      //   post_id     TIMEUUID,
      //   room_id     TEXT, 
      //   text        TEXT,
      //   PRIMARY KEY ((user_id), post_id)
      // ) WITH CLUSTERING ORDER BY (post_id DESC);
```

> Let's say that user "111..." has noticed the remark by "555..." and, perhaps a bit ashamed by their own boasting, wants to correct their assessment on the hike difficulty!

Looking at ```PRIMARY KEY ((user_id), post_id)```, we know that both **user_id** and **post_id** are used to define uniqueness of the row.
We'll need both to update our record (plus, of course, some of the data columns, otherwise we are not changing anything in that row!).

_You may remember that we used hardcoded values for **post_id** when we created these records (a real application would generate them live, one way or the other).
Imagine the UX for editing an existing post: when the user clicks the "edit" button, both **user_id** and **post_id** are known and can be provided to
the backend, where they ultimately become part of an **UPDATE** statement._

So we can run the following **UPDATE** statement and help user "111..." fix their post on table **_posts_by_user_**
(we also subsequently read back the data as a check):

📘 **Commands to execute**

```sql
UPDATE posts_by_user 
  SET text = '... and Mt. Gumbo was NOT SO easy!!!' 
    WHERE user_id = 11111111-1111-1111-1111-111111111111
    AND   post_id = aaaaaaaa-5cff-11ec-be16-1fedb0dfd057;

SELECT post_id, room_id, text FROM posts_by_user
  WHERE user_id = 11111111-1111-1111-1111-111111111111;
```

📗 **Expected output**

![Updating in CQL](images/cql/06_updated.png)

But **wait**: data, again, is denormalized! This means that we have to make sure
such an edit is performed on table **_posts_by_room_** as well.
Since the primary key of that table is given as `PRIMARY KEY ((room_id), post_id)`,
these are the fields to provide, along with `text` itself, to the **UPDATE** statement.

And we _could_ run an **UPDATE**. But, lo and behold, in Cassandra **UPDATE**s
and **INSERT**s are (almost) the same, as a consequence of its architecture and
the way storage and write logic are structured. We can then update the row with
an **INSERT** statement like the following (note that we provide: primary key +
any field that we want to modify; and leave out the other, unchanged fields):

📘 **Commands to execute**
```sql
INSERT INTO posts_by_room (room_id, post_id, text) VALUES (
  '#hiking',
  aaaaaaaa-5cff-11ec-be16-1fedb0dfd057,
  '... and Mt. Gumbo was NOT SO easy!!!'
);

SELECT post_id, user_id, text FROM posts_by_room WHERE room_id = '#hiking';
```

That's it, we successfully edited a post (on both tables).
All that's left now is to **DELETE** some data.

**✅ Step 3e. CRU(D) = delete = remove data**

The final operation from our **CRUD** acronym is **DELETE**. This is the operation we use when we want to remove data from the database.
In Apache Cassandra you can **DELETE** from the cell level all the way up to the partition
_(meaning I could remove a single column in a single row or I could remove a whole partition)_ using the same **DELETE** command.

_Generally speaking, it's best to perform as few delete operations as possible on the largest amount of data. Think of it this way, if you want to delete ALL data in a table, don't delete each individual cell, just **TRUNCATE** the table. If you need to delete all the rows in a partition, don't delete each row, **DELETE** the partition, and so on._

> User "555..." notices the post by "111..." being edited and wants to remove their snarky remark. Let's help them!

When deleting a row on a given table, we have to specify the values of the primary key for that table. And don't forget
that, in our data model, a post appears as two separate rows in the two tables, so we have to perform
two different **DELETE** operations!

📘 **Commands to execute**

```sql
SELECT post_id, room_id, text FROM posts_by_user
  WHERE user_id = 55555555-5555-5555-5555-555555555555;

SELECT post_id, user_id, text FROM posts_by_room WHERE room_id = '#hiking';

DELETE FROM posts_by_user
  WHERE user_id = 55555555-5555-5555-5555-555555555555
  AND post_id = bbbbbbbb-5cff-11ec-be16-1fedb0dfd057;

DELETE FROM posts_by_room
  WHERE room_id = '#hiking'
  AND post_id = bbbbbbbb-5cff-11ec-be16-1fedb0dfd057;

SELECT post_id, room_id, text FROM posts_by_user
  WHERE user_id = 55555555-5555-5555-5555-555555555555;

SELECT post_id, user_id, text FROM posts_by_room WHERE room_id = '#hiking';
```

(Notice in the above, for your convenience, we read the tables, then delete the rows, then read them again).

📗 **Expected output**

![Deleting in CQL](images/cql/07_deleting.png)

Notice the rows are now removed from both tables: it is as simple as that.

# Boom, motherfucker!