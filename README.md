# QOTD – Question of the Day Backend (FastAPI)

**Live API Docs:**  
[https://question-of-the-day-api.onrender.com/docs](https://question-of-the-day-api.onrender.com/docs)

A FastAPI-based backend service for a **Question of the Day (QOTD)** feature used in an edtech platform.  
Each day, a single DSA problem is published, users submit answers, and basic evaluation and statistics are recorded.


## Tech Stack
- **Language:** Python 3.11
- **Framework:** FastAPI
- **Server:** Uvicorn
- **ORM:** SQLAlchemy
- **Database:** SQLite
- **Validation:** Pydantic
- **Deployment:** Render

---

## Features
- One question per day (date-based uniqueness)
- Difficulty enforced using enums (easy / medium / hard)
- Structured examples with input, output, and explanation
- Answer submission with mock evaluation logic
- Per-user and per-question statistics
- RESTful APIs with Swagger documentation

---

##  Project Structure
```json
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
└── qotd.py
```

---

## 🗃️ Data Models

### QOTD
- `day_number` – Sequential identifier
- `date` – Unique date (one question per day)
- `title`, `difficulty`, `problem_statement`
- `examples` – Structured list of `{input, output, explanation}`
- `hints`, `constraints`
- `test_input`, `test_output`
- `solution`
- `attempts`, `correct_attempts`

### Submission
- `username`
- `user_answer`
- `status` (correct / incorrect)
- `attempts`, `correct_attempts`
- `submitted_at`

---
  
## API Endpoints

### Health Check
**GET /**  
```json
"QOTD API is working!"
```

### Upload Question of the Day

POST /upload_qotd

