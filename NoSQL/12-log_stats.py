#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def main(collection):
    """ log stats """

    # Get total number of logs
    num_logs = collection.count_documents({})

    # Define HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count documents for each method
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Count logs where method is GET and path is /status
    num_status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Display results
    print(f"{num_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    print(f"{num_status_check} status check for GET /status")

if __name__ == "__main__":
    # MongoDB connection
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    logs = db.nginx

    # Call the main function
    main(logs)
