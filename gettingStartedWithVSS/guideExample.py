import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<YOUR_SECURE_CONNECT_BUNDLE_PATH>>')
ASTRA_CLIENT_ID = '<<YOUR_CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<YOUR_CLIENT_SECRET>>'

KEYSPACE_NAME = 'vsearch'
TABLE_NAME = 'products'

print("Starting guide example")

cloud_config = {
   'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
#profile = ExecutionProfile(consistency_level=ConsistencyLevel.LOCAL_QUORUM)
#cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

print(f"Creating table {TABLE_NAME} in keyspace {KEYSPACE_NAME}")
session.execute(f"CREATE TABLE IF NOT EXISTS {KEYSPACE_NAME}.{TABLE_NAME} (id int PRIMARY KEY, name TEXT, description TEXT, item_vector VECTOR<FLOAT, 5>)")

print(f"Creating index ann_index on table {TABLE_NAME} and inserting example data")
session.execute(f"CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON {KEYSPACE_NAME}.{TABLE_NAME}(item_vector) USING 'StorageAttachedIndex'")

product_data = [
    (1, 'Coded Cleats', 'ChatGPT integrated sneakers that talk to you', [0.1, 0.15, 0.3, 0.12, 0.05]),
    (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [0.45, 0.09, 0.01, 0.2, 0.11]),
    (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [0.1, 0.05, 0.08, 0.3, 0.6])
]

for product in product_data:
    session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES {product}")

print(f"Returning 'nearest neighbor' using ANN search")
for row in session.execute(f"SELECT name, description, item_vector FROM {KEYSPACE_NAME}.{TABLE_NAME} ORDER BY item_vector ANN OF [0.15, 0.1, 0.1, 0.35, 0.55] LIMIT 1"):
   print("\t" + str(row))

cluster.shutdown()
