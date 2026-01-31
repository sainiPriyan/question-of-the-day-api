from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from datetime import date

router = APIRouter(tags=['Question of the day'])

@router.get('/')
def hello_world():
    return 'QOTD API is working!'

@router.post('/upload_qotd', response_model=schemas.QOTDResponse)
def upload_qotd(question: schemas.QOTD, db : Session = Depends(get_db)):

    query =  db.query(models.QOTD).filter(models.QOTD.date == date.today()).first()

    if query:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                             detail='Question already exists')
    
    question_data = question.model_dump()
    
    new_question = models.QOTD(**question_data)

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return new_question

@router.get('/problem_of_the_day', response_model=schemas.QOTDResponse)
def get_qotd(db: Session = Depends(get_db)):
    
    potd = db.query(models.QOTD).filter(models.QOTD.date == date.today()).first()

    if not potd:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    
    return potd

@router.post('/submit_answer_qotd')
def check_answer( request:schemas.SubmitAnswer , db: Session = Depends(get_db)):

    question = db.query(models.QOTD).filter(models.QOTD.date == date.today()).first()

    if not question:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)

    user = db.query(models.Submission).filter(models.Submission.username 
                                           == request.user.username).first()
    
    if not user:
        new_user = models.Submission(username=request.user.username,
                                     user_answer=str(request.output), status='incorrect')
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        user = new_user

    user.attempts += 1
    question.attempts += 1
    db.commit()

    if request.output == question.test_output:
        
        user.status = 'correct'
        user.correct_attempts += 1
        question.correct_attempts += 1
        db.commit()   
        acccuracy = (user.correct_attempts/user.attempts)*100
        average_accuracy = (question.correct_attempts/question.attempts)*100

 

        return {'Result':'Correct Answer!!', 'Accuracy': str(acccuracy)+'%',
                 'average_question_accuracy': str(average_accuracy)+'%',
                 'leaderboard_position': '3' }
    
    else:
        db.commit()
        return 'Incorrect Answer!'