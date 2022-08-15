#### 3. Register feature definitions and deploy the store

With the `apply` command, features defined in Python modules (in this case,
`example.py`) are scanned and used for actual deployment of the infrastructure.

Run the command
```
feast apply
```

> This is the step that actually accesses the database. After running it,
> you may want to check directly the presence of a new table in the Astra DB
> keyspace.