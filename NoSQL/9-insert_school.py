#!/usr/bin/env python3
"""
PyMongoDB
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document
    in a mongo collection
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
