from fastapi import FastAPI
from .graph import graph

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(req: dict):
    user_msg = req["message"]
    resp = await graph.ainvoke({"messages": [{"role": "user", "content": user_msg}]})
    return {"response": resp["messages"][-1].content}
