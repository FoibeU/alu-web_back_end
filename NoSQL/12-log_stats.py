from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Adjust if MongoDB is running on a different host/port
db = client['logs']
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})

# Count logs by HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Count logs with method "GET" and path "/status"
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

# Output the stats
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{get_status_count} status check for GET /status")
