# AuthEssay Beta

This repository contains a minimal prototype for the AuthEssay service. The backend exposes
an API endpoint that receives a report, generates follow up questions using GPT-4o and stores
both the report and the generated questions in a database.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Set your OpenAI API key in the environment:
   ```bash
   export OPENAI_API_KEY=your-key
   ```
3. Launch the API server:
   ```bash
   uvicorn app.main:app --reload --app-dir backend
   ```
4. Send a POST request to `/generate` with JSON body `{ "report_text": "..." }`.

The server stores data in `backend/app.db` using SQLite for local development.
