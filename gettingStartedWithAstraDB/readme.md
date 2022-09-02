# Overview of Astra DB
```ini
[beginner][database][apache cassandra]
```

> ⚠️ Difficulty: **`Beginner`, we don't expect you to know how to use Astra DB.**
>
> Time to complete: ~ 10 mins

Understand Astra DB and how it differs from its underlying technology, Apache Cassandra®.

You can use the Astra DB console and [APIs (REST, GraphQL, Document, gRPC)] to greatly simplify cloud-native Cassandra application development. Astra DB reduces deployment time from weeks to minutes, and delivers a combination of serverless, pay-as-you-go pricing with the freedom and agility of multi-cloud and open-source software. All that functionality is yours without the hassles of complex database and infrastructure administration.

### In this guide, we will
- What do I get with Astra DB?
- What are guardrails and how do they affect databases?
- What changes do I need to connect to Astra DB?
- Create an Astra database

### ~~Prerequisites~~
~~This is a placeholder to see what it looks like~~

## 1  What do I get with Astra DB?
DataStax [Astra DB] is built on Apache Cassandra®, the most reliable and scalable database in the world. **Astra DB** removes the pain of implementing and managing your own Apache Cassandra database. In addition of removing that complexity, we’ve also built a whole set of Drivers, APIs, and Integrations that will help you easily connect to your application.

### Under the hood
Creating a database within Astra provides you with a **[serverless]** database cluster built on Apache Cassandra® that starts with 3 nodes using a replication factor of 3.

By **"[serverless]"** we mean that **Astra** databases are elastic and can scale to meet your demands. **Astra** also separates storage and compute to keep TCO (Total Cost of Ownership) down. No need to pay for processing time if your application is in-between operations.

**Astra** currently supports deployment to all three major cloud providers (**GCP, AWS, Azure**) and provides a wide range of geographic [regions] for use around the world. You can also deploy to multiple regions within a single database. Click a button, pick a region, **Astra** handles deploying a new datacenter and replicates data for you.

Finally, **Astra** provides a whole set of tools and [APIs (REST, GraphQL, Document, gRPC)] to make it easy to hook up your application. Take a look at this [FAQ] to learn more.

## 2 What are guardrails and how do they affect databases?
Databases created within Astra DB are defined with a set of limits, called **[guardrails]**, that foster good practices and ensure your databases run optimally.

We strongly encourage you to read our documentation on [guardrails] for details.

_Existing open source Apache Cassandra® users might want to check out this [CEP](https://cwiki.apache.org/confluence/display/CASSANDRA/CEP-3%3A+Guardrails). Guardrails are planned..._


## 3 What changes do I need to connect to Astra DB?
OMG totally nothing. Just RTFM!

## 4 Create an Astra database 🔥
Let's start by creating an Astra database. Click the link/button/whatever below and follow the prompts to get started.

You'll be presented with four options

### Database name
The name you assign to your database. This is the name displayed within the Astra console.

### Keyspace name
Where all of your database tables are stored within the **database**. 

_If you're already an Apache Cassandra® user this is exactly the same as the keyspaces you are accustomed to and use a replication factor of 3._

### Cloud deployment **Provider** 
A list of the available cloud providers. Currently, Astra offers deployment to all three major providers `Google Cloud`, `Amazon Web Services`, and `Microsoft Azure`. 

_Free tier users are limited to selections with Google Cloud._

### Cloud deployment **region** 
The geographic region within the chosen cloud provider. Just pick one close to you for now.

_No cloud provider accounts are needed for any of the options presented. Astra handles all cloud provider deployments and details._

<<createDatabase>>

[APIs (REST, GraphQL, Document, gRPC)]: (https://docs.datastax.com/en/astra-serverless/docs/develop/developing.html)

[Astra DB]: (https://docs.datastax.com/en/astra-serverless/docs/)
[serverless]: (https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_serverless_databases)
[regions]: (https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#serverless-regions)
[consistency level]: (https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_cassandra_query_language_cql)
[faq]: (https://docs.datastax.com/en/astra-serverless/docs/astra-faq.html)
[APIs (REST, GraphQL, Document, gRPC)]: (https://docs.datastax.com/en/astra-serverless/docs/develop/developing.html)

[guardrails]: (https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_astra_db_database_guardrails_and_limits)