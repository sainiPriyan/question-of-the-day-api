from pydantic import BaseModel
from typing import List
from enum import Enum
from datetime import date

class Difficulty(str, Enum):

    easy = "easy"
    medium = "medium"
    hard = "hard"

class Example(BaseModel):

    input: str
    output: str
    explanation: str    

class QOTD(BaseModel):

    day_number: int
    date: date
    title: str
    difficulty: Difficulty

    problem_statement: str

    examples: List[Example]
    hints: List[str]

    constraints: List[str]

    test_input: List[str]
    test_output: List[str]

    solution: str

class QOTDResponse(BaseModel):

    day_number: int
    date: date
    title: str
    difficulty: str
    
    problem_statement: str

    examples: List[Example]
    hints: List[str]

    constraints: List[str]


class User(BaseModel):
    username: str
    name: str

class SubmitAnswer (BaseModel):
    user: User
    output: List[str]  
