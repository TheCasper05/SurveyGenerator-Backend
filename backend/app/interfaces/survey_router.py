from fastapi import APIRouter, Depends
from app.schemas.survey_schema import Survey, SurveyCreate, SurveyUpdate, QuestionCreate, Question
from app.dependencies.di import get_db
from sqlalchemy.orm import Session
from typing import List
from app.application.survey_service import survey_service



router = APIRouter()

@router.post("/surveys/", response_model=Survey)
def create_survey(survey:SurveyCreate, db:Session = Depends(get_db)):
    return survey_service.create_survey(db, survey)

@router.get("/surveys/", response_model=List[Survey])
def read_surveys(db: Session = Depends(get_db)):
    return survey_service.get_surveys(db)

@router.get("/surveys/{survey_id}", response_model= Survey)
def read_survey(survey_id: int, db:Session = Depends(get_db)):
    return survey_service.get_survey_by_id(db, survey_id)

@router.put("/surveys/{survey_id}", response_model= Survey)
def update_survey(survey_id: int, survey: SurveyUpdate, db: Session = Depends(get_db)):
    return survey_service.update_survey(db, survey_id, survey)

@router.delete("/surveys/{survey_id}")
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    return survey_service.delete_survey_by_id(db, survey_id)

@router.post("/surveys/{survey_id}/questions/", response_model= Question)
def create_question(survey_id: int, question: QuestionCreate, db: Session = Depends(get_db)):
    return survey_service.add_question_to_survey(db, survey_id, question)

@router.get("/surveys/{survey_id}/questions/", response_model=list[Question])
def list_questions_for_survey(survey_id: int, db: Session = Depends(get_db)):
    return survey_service.get_questions_for_survey(db, survey_id)

