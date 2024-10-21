#!/usr/bin/env python3
"""Task 15's module."""

from pymongo import MongoClient


def print_nginx(nginx_collection):
    """Prints stats about Nginx request logs."""
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


def print_top_ips(server_collection):
    """_summary_

    Args:
        server_collection (_type_): _description_
    """
    print("IPs:")
    request_logs = server_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}},
            {"$sort": {"totalRequests": -1}},
            {"$limit": 10},
        ]
    )
    for request_log in request_logs:
        ip = request_log["_id"]
        ip_requests_count = request_log["totalRequests"]
        print("\t{}: {}".format(ip, ip_requests_count))


def run():
    """_summary_
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx(client.logs.nginx)
    print_top_ips(client.logs.nginx)


if __name__ == "__main__":
    run()
