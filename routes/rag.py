import os
import sys
from fastapi import APIRouter,Form,UploadFile,File
from pydantic import BaseModel
from utils.rag_model import (queryRAGModel)
from utils.topics import (add_topic)
router=APIRouter(prefix="/rag")

class queryDAO(BaseModel):
    query:str | None = None
    topic_id:str

@router.post("/query")
def query_rag(body:queryDAO):
    try:
        req_body=body.__dict__
        print(req_body)
        return queryRAGModel(req_body)
    except Exception as e:
        print("Error occurred in rag query route - ",e)
        return {"status":'error',"error":e} 

@router.post("/enhance")
async def enhance_rag(title:str=Form(),description:str=Form(),topic:str=Form(),webResource:str=Form(...),poster:UploadFile=File()):
    try:
        req_body={
            "title":title,
            "description":description,
            "topic":topic,
            "webResource":webResource,
            "poster":poster
        }
        print(req_body,poster.filename)
        #response = await add_topic(req_body)
        return response
    except Exception as e:
        print("Error occurred in rag enhance route - ",e)
        return {"status":'error',"error":e}        
    