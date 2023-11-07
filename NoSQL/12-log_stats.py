#!/usr/bin/env python3
""" Write a Python script that provides 
    some stats about
    Nginx logs stored in MongoDB
"""


import pymongo


def log_stats():
    """
    Provides NGinx Statuses
    """

    client = pymongo.MongoClient()
    db = client.logs
    logs = db.nginx
    methods = ["GET", "PUT", "POST", "PATCH", "DELETE"]
    status = logs.count_documents({'method': 'GET', 'path': '/status'})

    #Prints the number of logs
    print(f"{logs.count_documents({})} logs")

    #Prints the number of methods
    print("Methods: ")
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    
    #Prints status check
    print(f"{status} status check")

if __name__ == "__main__":
    log_stats()