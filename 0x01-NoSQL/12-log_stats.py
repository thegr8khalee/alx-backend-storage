#!/usr/bin/env python3
"""Task 12: Log stats"""

from pymongo import MongoClient


def print_nginx(nginx_collection):
    """Prints stats about Nginx logs stored in MongoDB.

    Args:
        nginx_collection: pymongo collection object
    """
    # Print the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Print the count of each method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Print the count of status checks
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


def run():
    """Connects to MongoDB and prints Nginx log statistics."""
    # Connect to the MongoDB server
    client = MongoClient("mongodb://127.0.0.1:27017")

    # Get the 'nginx' collection from the 'logs' database
    nginx_collection = client.logs.nginx

    # Print Nginx log stats
    print_nginx(nginx_collection)


if __name__ == "__main__":
    run()
