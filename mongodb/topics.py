import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from db_config import (db)

def find_by_query(query,projection):
    try:
        topic_collection=db["topics"]
        ret=list(topic_collection.find(query,projection))
        print(ret)
        return {"status":"success","data":ret}
    except Exception as e:
        print("Error occurred while fetching topics from DB",e)
        return{"status":"error","message":"Error occurred while fetching topics from DB"}   

def find_one_by_query(query):
    try:
        topic_collection=db["topics"]
        ret=dict(topic_collection.find_one(query))
        print(ret)
        return {"status":"success","data":ret}
    except Exception as e:
        print("Error occurred while fetching topics from DB",e)
        return{"status":"error","message":"Error occurred while fetching topics from DB"}            

def insert_record(record):
    try:
        topic_collection=db["topics"]
        record_id=topic_collection.insert_one(record)
        if(record_id):
            return {"status":"success","message":"topic successfully inserted"}
        else:
            return{"status":"error","message":"Error occurred while inserting record to DB"}
    except Exception as e:
        print("Error occurred while inserting record to DB",e)
        return{"status":"error","message":"Error occurred while inserting record to DB"}

