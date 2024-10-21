#!/usr/bin/env python3
"""README.md"""


def insert_school(mongo_collection, **kwargs):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
    """
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
