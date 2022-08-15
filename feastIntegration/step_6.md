#### 6. Fetch feature vectors from the online store

The `get_online_features` store method will query the online store
and return the required features, as resulting from the last
"materialize" operation.

Create a `fetch_online.py` script and run it with `python fetch_online.py`:

<details><summary>Show "fetch_online.py"</summary>

```python
from pprint import pprint
from feast import FeatureStore

store = FeatureStore(repo_path=".")

feature_vector = store.get_online_features(
    features=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips",
    ],
    entity_rows=[
        # {join_key: entity_value}
        {"driver_id": 1004},
        {"driver_id": 1005},
    ],
).to_dict()

pprint(feature_vector)
```

</details>