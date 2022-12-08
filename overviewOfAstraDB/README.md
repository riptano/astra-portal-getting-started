# Overview
Astra DB is a serverless database service (DBaaS) built on Apache Cassandra®. 

You can use the Astra DB console and [APIs (REST, GraphQL, Document, gRPC)](https://docs.datastax.com/en/astra-serverless/docs/develop/developing.html) to greatly simplify cloud-native Cassandra application development. Astra DB reduces deployment time from weeks to minutes, and delivers a combination of serverless, pay-as-you-go pricing with the freedom and agility of multi-cloud and open-source software. All that functionality is yours without the hassles of complex database and infrastructure administration.

**In this guide, we'll learn**
- What do I get with Astra DB?
- What are guardrails and how do they affect databases?
- What changes do I need to connect my application to Astra DB?
- How to Create an Astra database with the UI 🔥

## 1  What do I get with Astra DB?
DataStax [Astra DB](https://docs.datastax.com/en/astra-serverless/docs/) is built on Apache Cassandra, the most reliable and scalable database in the world. Astra DB removes the pain of implementing and managing your own Apache Cassandra database. In addition of removing that complexity, we’ve also built a whole set of Drivers, APIs, and Integrations that will help you easily connect to your application.

### Under the hood
Creating a database within Astra provides you with a **[serverless](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_serverless_databases)** database cluster built on Apache Cassandra and starts using a replication factor of 3.

By **"[serverless](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_serverless_databases)"** we mean that **Astra** databases are elastic and can scale to meet your demands. **Astra** also separates storage and compute to keep Total Cost of Ownership (TCO) down. No need to pay for processing time if your application is in-between operations.

Astra currently supports deployment to all three of the major cloud providers: GCP, AWS, and Azure. Those providers provide a wide range of geographic [regions](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#serverless-regions) for use around the world. You can also deploy to multiple regions within a single database. Click a button, pick a region, and Astra handles deploying a new datacenter and replicates data for you.

Finally, **Astra** provides a whole set of tools and [APIs (REST, GraphQL, Document, gRPC)](https://docs.datastax.com/en/astra-serverless/docs/develop/developing.html) to make it easy to hook up your application. Take a look at this [FAQ](https://docs.datastax.com/en/astra-serverless/docs/astra-faq.html) to learn more.

## 2 What are guardrails and how do they affect databases?
[Guardrails](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_astra_db_database_guardrails_and_limits) are a set of limits for all databases created within Astra DB. Guardrails foster good practices, and ensure your databases run optimally.

Here are some examples of guardrails:
- [The size of values allowed in a single column](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_columns)
- [The number of Storage Attached Indexes you can have per table](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_storage_attached_indexing_sai_limits)
- [Rate-limiting](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_workloads)

We strongly encourage you to read our documentation on [guardrails](https://docs.datastax.com/en/astra-serverless/docs/plan/planning.html#_astra_db_database_guardrails_and_limits) for details.

## 3 What changes do I need to connect my application to Astra DB?
That depends on whether you are a first time user to Apache Cassandra and Astra, or if you have an existing implementation.

### Existing Apache Cassandra implementation using drivers
If you have an existing application using the DataStax drivers connected to an open source Apache Cassandra cluster you'll need to ensure you are using an Astra compatible driver. Follow the instructions [here for information on each supported language](https://docs.datastax.com/en/astra-serverless/docs/connect/drivers/migrating-datastax-drivers-to-connect-to-astra-databases.html). Changes are usually often minimal and once in place will usually switch from providing your username, password, and a set of seed nodes to providing a secure connect bundle that contains everything needed to securely connect to Astra.

### First time Apache Cassandra/Astra user or looking for options other than drivers
If you're new to Apache Cassandra and Astra, or looking for other options you have multiple choices.

#### Drivers
[Astra drivers](https://docs.datastax.com/en/astra-serverless/docs/getting-started/gs-drivers.html) have the best performance and configuration options. But with that comes more complexity and the need to maintain driver versions in application code. If you are looking for a performant and "lightweight" HTTP based alternative to drivers, [gRPC](https://docs.datastax.com/en/astra-serverless/docs/develop/dev-with-grpc.html) is a good option.

#### Stargate APIs
The Stargate APIs consist of [REST, GraphQL, Document, and gRPC](https://docs.datastax.com/en/astra-serverless/docs/develop/developing.html). These are all "driverless" methods of connecting to Astra. All are provided by Astra.
- [REST API](https://docs.datastax.com/en/astra-serverless/docs/develop/dev-with-rest.html) - Pretty much the standard way to handle HTTP based application communications
- [GraphQL API](https://docs.datastax.com/en/astra-serverless/docs/develop/graphql.html) - Extremely flexible table and payload definitions. Originally developed for mobile communications to keep payload sizes down. Allows chaining of multiple queries into a single result payload (think about having control you wish you had with REST). 
- [Document API](https://docs.datastax.com/en/astra-serverless/docs/develop/dev-with-doc.html) - Native storage, retrieval, and manipulation of JSON documents
- [gRPC](https://docs.datastax.com/en/astra-serverless/docs/develop/dev-with-grpc.html) - A cloud native "lightweight" and fast client that allows direct CQL calls (on par performance with native drivers)

## 4 How to Create an Astra database with the UI 🔥
Now that you have a better idea of what to consider when using Astra, let's get you started by creating an Astra database.

You'll be presented with four options

### Database name
The name you assign to your database. This is the name displayed within the Astra console.

### [Keyspace](https://docs.datastax.com/en/astra-serverless/docs/manage/db/manage-keyspaces.html) name
Where all of your database tables are stored within the **database**. 

_If you're already an Apache Cassandra user this is exactly the same as the keyspaces you are accustomed to and use a replication factor of 3._

### Cloud deployment **Provider** 
A list of the available cloud providers. Currently, Astra offers deployment to all three major providers **_Google Cloud_**, **_Amazon Web Services_**, and **_Microsoft Azure_**. 

_Free tier users are limited to selections with Google Cloud._

### Cloud deployment **region** 
The geographic region within the chosen cloud provider. Just pick one close to you for now.

_No cloud provider accounts are needed for any of the options presented. Astra handles all cloud provider deployments and details._

Click the button below to create a database.

<<createDatabase>>

## 5 Summary
Ok, great! You have a database and you know a bit more about Astra DB. Now it's time to start working with some data, and hook up your app.

Feel free to explore **_CRUD operations_** in the recommended guide below, or check out our list of **_integrations_** and **_sample apps_** in the navigation to the left.

All are designed to help connect your app quickly and easily, so you can focus on building something awesome. We'll handle the data.

Happy building! 🚀

