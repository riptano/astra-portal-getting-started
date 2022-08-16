## A - Overview

```ini
[beginner][Python][database][machine learning]
```

> ⚠️ Difficulty: **`Beginner`, we don't expect you to know how to integrate Feast with Astra.**
>
> Time to complete: ~ 10 mins

[Feast](https://feast.dev/)
is a (Apache-licensed) open-source feature store for machine learning.
Feast aims at providing a fast solution to the typical MLOps needs one encounters
when bringing ML applications to production.

Feast offers a solution to the problem of training/serving skew, provides tools
to standardize the data engineering workflows (thus avoiding having to
"re-invent the features" every time), and ensures reproducible feature sets with
point-in-time historical retrievals.

This feature store supports several backends, both as offline store (for historical
time-series data) and online store (with the latest features, synced from the former
by Feast itself). Some of the backends are native in Feast, but several more are
available as external plugins. Feast is built with the cloud in mind: one of its
goals is to free MLOps practitioners and data engineers from having to manage
their own infrastructure.

In this spirit, the
[Feast online store plugin for Cassandra](https://pypi.org/project/feast-cassandra/)
flexibly supports
both Cassandra and Astra DB, as will be explained below.

Reference documentation:

- ℹ️ [Feast documentation](https://docs.feast.dev/)
- ℹ️ [Minimal quickstart with Feast](https://docs.feast.dev/getting-started/quickstart)
- ℹ️ [The `feast-cassandra` plugin](https://pypi.org/project/feast-cassandra/)

## B - Prerequisites
### Create database
<<CreateDBButton>> 
```
PARAMS NEEDED
databaseName: feast
keyspaceName: feastks
region: closest in free tier
```

### Create Token
<<CreateToken>> 
```
PARAMS NEEDED
role: "Database Administrator"
```

### Download SCB
<<DownloadSCB>> 
```
PARAMS NEEDED
region: region of created database
```

### Install Feast
<<REPLIT>> 
```
PARAMS NEEDED
langauge: python
command: pip install feast feast-cassandra
```
- Install Feast and the Cassandra/Astra DB plugin in your local Python environment, i.e. `pip install feast feast-cassandra`. See the specific pages ([Feast](https://docs.feast.dev/getting-started/quickstart#step-1-install-feast), [Cassandra plugin](https://pypi.org/project/feast-cassandra/)) for additional installation info.


## C - Quickstart

_Note: this quickstart is modeled after the one
found in the
[Feast documentation](https://docs.feast.dev/getting-started/quickstart).
The numbering of the steps is chosen to be consistent with it.
All credits for the sample code given here goes to the Feast documentation._

A new feature store is created and configured to use Astra DB as online store;
next, it will be materialized to database using sample feature definitions and
sample data; finally, historical/online feature retrieval is demonstrated.
