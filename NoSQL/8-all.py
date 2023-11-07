#!/usr/bin/env python3
"""
List all mongo
in python
"""

import pymongo


def list_all(mongo_collection):
    """
    Lists all documents
    in a collection
    """
    documents = mongo_collection.find()
    return documents
