# backend/llm_setup.py

import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

# 🧠 Initialize the OpenAI Chat LLM
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

# 🛠 Define the prompt structure the agent will use
system_prompt = "You are a helpful assistant that books events in the user's calendar."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="messages")
])
# The llm_chain will invoke the LLM with the given prompt + messages
llm_chain = prompt | llm
