import os

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<PATH_TO_YOUR SECURE_BUNDLE>>')
ASTRA_CLIENT_ID = '<<YOUR_CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<YOUR_CLIENT_SECRET>>'
KEYSPACE_NAME = 'vsearch'
TABLE_NAME = 'products'

print("Staring guide example")
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel

cloud_config = {
   'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)

profile = ExecutionProfile(
    consistency_level=ConsistencyLevel.LOCAL_QUORUM,
)

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
session = cluster.connect()

# Create the products table with VECTOR support
print(f"Creating table {TABLE_NAME} in keyspace {KEYSPACE_NAME}")
session.execute(f"CREATE TABLE IF NOT EXISTS {KEYSPACE_NAME}.{TABLE_NAME} (id int PRIMARY KEY, name varchar, description varchar, item_vector VECTOR<float, 3>)")

# Create an ANN index on the VECTOR field
print(f"Creating index ann_index on table {TABLE_NAME} and inserting example data")
session.execute(f"CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON {KEYSPACE_NAME}.{TABLE_NAME}(item_vector) USING 'StorageAttachedIndex'")

# Insert a few example rows including VECTOR data
session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES (1, 'Coded Cleats', 'ChatGPT integrated sneakers that talk to you', [8, 2.3, 58])")
session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [1.2, 3.4, 5.6])")
session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [23, 18, 3.9])")

# Using an ANN search, find the 'nearest neighbors' closest to the provided vector [3.4, 7.8, 9.1]
print(f"Returning 'nearest neighbor' using ANN search")
for row in session.execute(f"SELECT name, description, item_vector FROM {KEYSPACE_NAME}.{TABLE_NAME} ORDER BY item_vector ANN OF [3.4, 7.8, 9.1] LIMIT 1"):
   print("\t" + str(row))

# Close the connection
cluster.shutdown()
