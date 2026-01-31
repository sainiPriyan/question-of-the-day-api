from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, JSON
from sqlalchemy.orm import relationship
import datetime

class QOTD(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    day_number = Column(Integer, unique=True, index=True)
    date = Column(Date, default=datetime.date.today, unique=True, index=True)
    title = Column(String)
    difficulty = Column(String)  # Easy, Medium, Hard
    problem_statement = Column(String)
    examples = Column(JSON)  
    hints = Column(JSON)     
    constraints = Column(JSON) 
    test_input = Column(JSON)  
    test_output = Column(JSON)
    solution = Column(String)
    attempts = Column(Integer,default=0)
    correct_attempts = Column(Integer,default=0)  

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique= True)
    attempts = Column(Integer,default=0)
    correct_attempts = Column(Integer,default=0)
    user_answer = Column(String)
    status = Column(String)  # Correct, Incorrect, Partially Correct
    submitted_at = Column(Date, default=datetime.date.today)    