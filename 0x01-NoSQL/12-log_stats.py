#!/usr/bin/env python3
"""Task 12: Log stats"""

from pymongo import MongoClient


def print_nginx(nginx_collection):
    """_summary_

    Args:
        nginx_collection (_type_): _description_
    """
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        req_count = len(list(nginx_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, req_count))
    status_checks_count = len(
        list(nginx_collection.find({"method": "GET", "path": "/status"}))
    )
    print("{} status check".format(status_checks_count))


def run():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx(client.logs.nginx)


if __name__ == "__main__":
    run()
