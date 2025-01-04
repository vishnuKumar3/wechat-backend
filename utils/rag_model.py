from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import (WebBaseLoader)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from uuid import uuid4
from bs4 import BeautifulSoup
from mongodb import (topics)
from pinecone import Pinecone
import os

def fetch_vector_store():
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    index=pc.Index("genai-project")

    embedingModel=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=PineconeVectorStore(index=index,embedding=embedingModel)
    return vector_store

def fetch_LLM():
    return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=200,
            timeout=None,
            max_retries=2,
        )    

def queryRAGModel(payload):
    try:
        query=payload.get("query") or "Hii"
        topic_info = topics.find_one_by_query({"topicId":payload.get("topic_id")})
        if(topic_info.get("status") and topic_info.get("status").lower()=="success" and topic_info.get("data")):
            topic_record = topic_info.get("data")
            metadata=topic_record.get("metadata")
            vector_store=fetch_vector_store()
            similar_docs=vector_store.similarity_search(query,filter={"source":metadata.get("source")})
            print("similar_docs length -",len(similar_docs))
            context=""
            for i in similar_docs:
                context+=i.page_content
                context+=" "
            llm = fetch_LLM()
            messages=[
                SystemMessage(content=f'''You are a RAG model, capable of analyzing context and produce text based on the user query.
                              If the query is within context - 
                                you will produce accurate results for the query based on the given context only. 
                              else if the intent of the query related to the current context - 
                                you will answer in your own way
                              else - 
                                please reply in a formal way that it is out of your knowledge in a creative way.
                              Finally the context is as follows:
                            {context}
                            '''),
                HumanMessage(content=f"{query}")
            ]
            response=llm.invoke(messages)
            return {"status":"success","data":response.content}
        else:
            return topic_info

    except Exception as e:
        print("Error occurred in RAG model - ",e)
        return {"status":'error',"error":e}
    
def enhance_RAG_knowledge(req_data):
    try:
        loader=WebBaseLoader(req_data["web_URL"])
        docs=loader.load()
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
        documents=text_splitter.split_documents(docs)
        print("total documents after split - ",len(documents))    
        vector_store=fetch_vector_store()
        uuids = [str(uuid4()) for _ in range(len(documents))]
        document_ids=vector_store.add_documents(documents=documents,ids=uuids)
        print(documents[0].metadata)
        if(len(document_ids)>0):
            return {"status":"success","message":"successfully updated the RAG knowledge","metadata":documents[0].metadata}
        else:
            return {"status":"error","message":"Error occurred while enhancing RAG knowledge"}
    except Exception as e:
        print("Error occurred while enhancing RAG knowledge",e)
        return {"status":"error","message":"Error occurred while enhancing RAG model knowledge"}        

