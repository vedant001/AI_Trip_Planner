from fastapi import FastAPI
from agent.agentic_workflow import GraphBuilder 
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app=FastAPI()


class QueryRequest(BaseModel):
    query:str
    
@app.post("/query"):

async def query_travel_agent(query: QueryRequest):
    try:
        graph=GraphBuilder(model_provider="groq")
        react_graph=graph()