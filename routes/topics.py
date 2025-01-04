from fastapi import APIRouter
from utils.topics import (fetch_topics)

router=APIRouter(prefix="/topics",tags=["topics"])

@router.post("/fetch")
def fetch():
    try:
        return fetch_topics()
    except Exception as e:
        print("Error occurred while fetching topics route",e)
        return {
            "status":"error",
            "message":"Error occurred while fetching topics route"
        }
