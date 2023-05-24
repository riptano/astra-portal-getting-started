import os

# Replace these values with the path to your secure connect bundle and the database credentials
SECURE_CONNECT_BUNDLE_PATH = os.path.join(os.path.dirname(__file__), '<<PATH_TO_YOUR_SECURE_BUNDLE>>')
ASTRA_CLIENT_ID = '<<CLIENT_ID>>'
ASTRA_CLIENT_SECRET = '<<CLIENT_SECRET>>'
KEYSPACE_NAME = 'vector_example'
TABLE_NAME = 'products'

#import logging

print("Staring guide example")

#log = logging.getLogger()
#log.setLevel('INFO')

#handler = logging.StreamHandler()
#handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
#log.addHandler(handler)

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Create a table using Vector Search
print("Creating table with VSS support")
session.execute("CREATE TABLE {KEYSPACE_NAME}.{TABLE_NAME}( \
                    id UUID PRIMARY KEY, \
                    name varchar, \
                    description varchar, \
                    item_vector float vector[3]); ")

# Create an index an ANN (Approximate Nearest Neighbor) on our Vector field
print("Creating index using ANN (Approximate Nearest Neighbor)")
session.execute("CREATE CUSTOM INDEX ann_index \
                    ON {KEYSPACE_NAME}.{TABLE_NAME}(item_vector) \
                    USING 'StorageAttachedIndex' ")

# Insert some example Vectors
print("Inserting example vectors")
session.execute("INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, item_vector) values (1, [8, 2.3, 58])")
session.execute("INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, item_vector) values (2, [1.2, 3.4, 5.6])")
session.execute("INSERT INTO {KEYSPACE_NAME}.{TABLE_NAME} (id, item_vector) values (5, [23, 18, 3.9])")

# Using an ANN search, find the 'nearest neighbors' closest to the provided vector [3.4, 7.8, 9.1]
print("Reading nearest neighbors")
for row in session.execute("SELECT item_vector \
                            FROM {KEYSPACE_NAME}.{TABLE_NAME} \
                            WHERE item_vector ANN OF [3.4, 7.8, 9.1] LIMIT 1; "):
    results = row[0]
    assert len(results) == 3
    print(results)

# Close the connection
cluster.shutdown()