#### 2. Create a feature repository

In a directory of your choice, create a new repository and `cd` to the
corresponding directory:

```
feast init astra_feature_repo
cd astra_feature_repo
```

As you can see, the new feature store already contains sample data
and a sample feature definition. These will be used in this walkthrough,
so don't delete them.

#### 2B. Configure Astra DB as online store

Locate and open the store configuration file, `feature_store.yaml`. Replace
the `online_store` portion of the file with something like (_use your values
for the bundle path and the token authentication info_):

```
online_store:
    type: feast_cassandra_online_store.cassandra_online_store.CassandraOnlineStore
    secure_bundle_path: /path/to/secure/bundle.zip
    username: Client_ID
    password: Client_Secret
    keyspace: feastks
```

<details><summary>Settings in "feature_store.yaml" for usage with Cassandra</summary>

If using regular Cassandra as opposed to Astra DB, the "online_store" portion might look like:

```
online_store:
    type: feast_cassandra_online_store.cassandra_online_store.CassandraOnlineStore
    hosts:
        - 192.168.1.1
        - 192.168.1.2
        - 192.168.1.3
    keyspace: feastks
    port: 9042        # optional
    username: user    # optional
    password: secret  # optional
```
</details>