# Calendar Booking Agent

## Overview
A conversational AI to book appointments via Google Calendar:

- **Backend**: FastAPI + LangGraph + Google Calendar integration  
- **Frontend**: Streamlit chat interface

## Project Structure
calendar_agent/
├── README.md
├── requirements.txt
├── .env
├── credentials.json
├── token.json
├── backend/
│ ├── init.py
│ ├── main.py
│ ├── graph.py
│ ├── llm_setup.py
│ ├── calendar_toolkit.py
│ ├── context_manager.py
│ └── utils.py
└── frontend/
├── init.py
└── app.py
