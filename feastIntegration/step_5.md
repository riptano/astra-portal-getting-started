#### 5. Load features in the online store

With the `materialize-incremental` command, Feast is instructed
to carry the latest feature values over to the online store, for
quick access during feature serving:

```
CURRENT_TIME=$(date -u +"%Y-%m-%dT%H:%M:%S")
feast materialize-incremental $CURRENT_TIME
```

> At this point, inspection of the Astra DB table will show the presence of
> newly-inserted rows.