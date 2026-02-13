from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Replace with your MongoDB URI
MONGO_URI = "mongodb://localhost:27017"

try:
    # Create client
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

    # Trigger connection test
    client.admin.command("ping")

    print("✅ Connected to MongoDB successfully")

    # List databases
    dbs = client.list_database_names()
    print("Databases:", dbs)

except ConnectionFailure as e:
    print("❌ MongoDB connection failed")
    print(e)
