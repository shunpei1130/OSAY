# AuthEssay Beta

This repository contains a prototype for the AuthEssay service.  The backend now
lets students submit reports, answer automatically generated questions and see
their pass/fail result.  A simple dashboard API lists all submissions for
teachers.

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
4. Submit a report:
   ```bash
   curl -X POST http://localhost:8000/generate -H 'Content-Type: application/json' \
     -d '{"username": "alice", "report_text": "..."}'
   ```
   This returns the generated questions and a `report_id`.
5. After answering the questions, send them back to `/submit_answers`:
   ```bash
   curl -X POST http://localhost:8000/submit_answers -H 'Content-Type: application/json' \
     -d '{"username": "alice", "report_id": 1,
          "answers": [{"question_id": 1, "text": "..."}]}'
   ```
   The response includes the grading result.
6. Teachers can query `/dashboard` to list all submissions.

The server stores data in `backend/app.db` using SQLite for local development.
