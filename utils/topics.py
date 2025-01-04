import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from pymongo import MongoClient
from mongodb import (topics)
import cloudinary
import cloudinary.uploader
from bson import ObjectId
from rag_model import enhance_RAG_knowledge


async def add_topic(req_data):
    try:
        result=enhance_RAG_knowledge({"web_URL":req_data["webResource"] or ""})
        if(result.get("status")!=None and result["status"].lower()=="success" and result.get("metadata")!=None):
            poster=req_data["poster"]
            del req_data["poster"]
            req_data["metadata"]=result["metadata"] or {}
            file_data=await poster.read()
            object_id = ObjectId()
            upload_result = cloudinary.uploader.upload(file_data,public_id=req_data["title"],display_name=req_data["title"],asset_folder="WeChat", resource_type="auto")
            req_data["poster"]=upload_result.get("url")
            req_data["_id"]=object_id
            req_data["topicId"]=str(object_id)
            print("file upload result",upload_result)
            print(req_data)
            result=topics.insert_record(req_data)
            return result
        else:
            return result         
    except Exception as e:
        print("Error occurred in add topic function",e)
        return {
            "status":"error",
            "message":e
        }
    
def fetch_topics():
    try:
        return topics.find_by_query({},{"metadata":0,"_id":0})
    except Exception as e:
        print("Error occurred in fetch topics function",e)
        return {
            "status":"error",
            "message":e
        }
    
