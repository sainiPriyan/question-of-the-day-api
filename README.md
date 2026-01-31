# QOTD – Question of the Day Backend (FastAPI)

**Live API Docs:**  
[https://question-of-the-day-api.onrender.com/docs](https://question-of-the-day-api.onrender.com/docs)

**Live API:**  
[https://question-of-the-day-api.onrender.com](https://question-of-the-day-api.onrender.com)

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



## Features
- One question per day (date-based uniqueness)
- Difficulty enforced using enums (easy / medium / hard)
- Structured examples with input, output, and explanation
- Answer submission with mock evaluation logic
- Per-user and per-question statistics
- RESTful APIs with Swagger documentation

## Improvements With More Time

- Secure sandboxed code execution
- Multiple test cases with partial scoring
- Authentication and user profiles
- PostgreSQL with Alembic migrations
- Real leaderboard and analytics dashboard
- Admin interface for scheduling QOTDs

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



## Data Models

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


  
## API Endpoints

### Health Check

**GET /**  

```json
"QOTD API is working!"
```

### Upload Question of the Day

**POST /upload_qotd**

```json
{
  "day_number": 1,
  "date": "2026-01-31",
  "title": "Two Sum",
  "difficulty": "easy",
  "problem_statement": "Given an array of integers...",
  "examples": [
    {
      "input": "[2,7,11,15], 9",
      "output": "[0,1]",
      "explanation": "nums[0] + nums[1] = 9"
    }
  ],
  "hints": ["Use a hashmap"],
  "constraints": ["1 <= n <= 10^5"],
  "test_input": ["[2,7,11,15],9"],
  "test_output": ["[0,1]"],
  "solution": <code snippet>"
}
```

### Get Today’s Question

**GET /problem_of_the_day**

```json
{
  "day_number": 1,
  "date": "2026-01-31",
  "title": "Two Sum",
  "difficulty": "easy",
  "problem_statement": "...",
  "examples": [...],
  "hints": [...],
  "constraints": [...]
}
```

### Submit Answer

**POST /submit_answer_qotd**

```json
{
  "user": {
    "username": "alice",
    "name": "Alice"
  },
  "output": ["[0,1]"]
}
```

Response:

```json
{
  "Result": "Correct Answer!!",
  "Accuracy": "100%",
  "average_question_accuracy": "75%",
  "leaderboard_position": "3"
}
```


### Run Locally
```json
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 10000
```
Open Swagger UI:
```json
http://localhost:10000/docs
```

