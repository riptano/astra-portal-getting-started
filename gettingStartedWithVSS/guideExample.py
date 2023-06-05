import os
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel

SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), 'secure-connect-for-silas-death.zip')
ASTRA_CLIENT_ID = 'ZZHNzjGieeeQNyhIjuFDZlwy'
ASTRA_CLIENT_SECRET = 'H5N,dXy8TbpNaWxWqme9qh_gpEH8b,IWnELaGRRufofEUGkQie53OG9b3bsTYGmZz1TciKc+Nwz85pIBgLDR_GChjjXvZh06BhqbOGbtOiScnZu3JMq4MiRr8fl5IPPm'
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
session.execute(f"CREATE TABLE IF NOT EXISTS {KEYSPACE_NAME}.{TABLE_NAME} (id int PRIMARY KEY, name varchar, description varchar, item_vector VECTOR<float, 3>)")

print(f"Creating index ann_index on table {TABLE_NAME} and inserting example data")
session.execute(f"CREATE CUSTOM INDEX IF NOT EXISTS ann_index ON {KEYSPACE_NAME}.{TABLE_NAME}(item_vector) USING 'StorageAttachedIndex'")

product_data = [
    (1, 'Coded Cleats', 'ChatGPT integrated sneakers that talk to you', [8, 2.3, 58]),
    (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [1.2, 3.4, 5.6]),
    (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', [23, 18, 3.9])
]

for product in product_data:
    session.execute(f"INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, name, description, item_vector) VALUES {product}")

print(f"Returning 'nearest neighbor' using ANN search")
for row in session.execute(f"SELECT name, description, item_vector FROM {KEYSPACE_NAME}.{TABLE_NAME} ORDER BY item_vector ANN OF [3.4, 7.8, 9.1] LIMIT 1"):
   print("\t" + str(row))

cluster.shutdown()
